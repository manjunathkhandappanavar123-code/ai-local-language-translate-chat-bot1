# model.py  –  AI-powered backend using Google Gemini

import os
import re
import json
import random
from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# SETUP GEMINI
# --------------------------------------------------

load_dotenv()
_api_key = os.getenv("GOOGLE_API_KEY", "").strip()

# Use the new google.genai SDK with confirmed working model
_MODEL_NAME = "gemini-flash-lite-latest"
_client = genai.Client(api_key=_api_key) if _api_key else None


def _ask_gemini(prompt: str, fallback: str = "") -> str:
    """
    Send a prompt to Gemini and return the text response.
    Falls back to `fallback` string on any error.
    """
    if _client is None:
        return fallback or "AI unavailable (API key missing)."
    try:
        response = _client.models.generate_content(
            model=_MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as exc:
        return fallback or f"AI error: {exc}"


# --------------------------------------------------
# LANGUAGE DATA  (fallback when Gemini is unavailable)
# --------------------------------------------------

VOCAB_DATA = {
    "Kannada": [
        ("Hello", "ನಮಸ್ಕಾರ"), ("Thank You", "ಧನ್ಯವಾದ"), ("Water", "ನೀರು"),
        ("Food", "ಆಹಾರ"), ("Mother", "ತಾಯಿ"), ("Father", "ತಂದೆ"),
        ("School", "ಶಾಲೆ"), ("Book", "ಪುಸ್ತಕ"), ("Name", "ಹೆಸರು"),
        ("Love", "ಪ್ರೀತಿ"),
    ],
    "Hindi": [
        ("Hello", "नमस्ते"), ("Thank You", "धन्यवाद"), ("Water", "पानी"),
        ("Food", "खाना"), ("Mother", "माँ"), ("Father", "पिताजी"),
        ("School", "स्कूल"), ("Book", "किताब"), ("Name", "नाम"),
        ("Love", "प्यार"),
    ],
    "Tamil": [
        ("Hello", "வணக்கம்"), ("Thank You", "நன்றி"), ("Water", "தண்ணீர்"),
        ("Food", "உணவு"), ("Mother", "அம்மா"), ("Father", "அப்பா"),
        ("School", "பள்ளி"), ("Book", "புத்தகம்"), ("Name", "பெயர்"),
        ("Love", "அன்பு"),
    ],
    "Telugu": [
        ("Hello", "నమస్కారం"), ("Thank You", "ధన్యవాదాలు"), ("Water", "నీరు"),
        ("Food", "ఆహారం"), ("Mother", "అమ్మ"), ("Father", "నాన్న"),
        ("School", "పాఠశాల"), ("Book", "పుస్తకం"), ("Name", "పేరు"),
        ("Love", "ప్రేమ"),
    ],
    "Malayalam": [
        ("Hello", "നമസ്കാരം"), ("Thank You", "നന്ദി"), ("Water", "വെള്ളം"),
        ("Food", "ഭക്ഷണം"), ("Mother", "അമ്മ"), ("Father", "അച്ഛൻ"),
        ("School", "വിദ്യാലയം"), ("Book", "പുസ്തകം"), ("Name", "പേര്"),
        ("Love", "സ്നേഹം"),
    ],
    "Marathi": [
        ("Hello", "नमस्कार"), ("Thank You", "धन्यवाद"), ("Water", "पाणी"),
        ("Food", "जेवण"), ("Mother", "आई"), ("Father", "बाबा"),
        ("School", "शाळा"), ("Book", "पुस्तक"), ("Name", "नाव"),
        ("Love", "प्रेम"),
    ],
}

GRAMMAR_DATA = {
    "Nouns": "Nouns are naming words. In most Indian languages, nouns have gender (masculine/feminine) and number (singular/plural). Example in Kannada: ಮನೆ (mane) = house.",
    "Pronouns": "Pronouns replace nouns. Common pronouns: I, You, He, She, We, They. In Hindi: मैं (main) = I, आप (aap) = you (formal), वह (vah) = he/she.",
    "Verbs": "Verbs express actions. In Indian languages, verbs agree with the subject in gender and number. Example: Tamil: போகிறேன் (I go), போகிறாய் (you go).",
    "Adjectives": "Adjectives describe nouns. They usually come before the noun in Indian languages. Example Telugu: పెద్ద (pedda) = big, చిన్న (chinna) = small.",
    "Adverbs": "Adverbs modify verbs, adjectives, or other adverbs. Example Malayalam: വേഗം (vegam) = quickly, ശരിയായി (shariyaayi) = correctly.",
    "Tenses": "Most Indian languages have Past, Present, and Future tenses. Tense markers are attached to the verb root. Example Hindi: जाना (jaana) = to go → गया (past), जाता हूँ (present), जाऊँगा (future).",
    "Sentence Formation": "Basic sentence order in Indian languages is Subject-Object-Verb (SOV). Example Kannada: ನಾನು ನೀರು ಕುಡಿಯುತ್ತೇನೆ = I water drink (I drink water).",
    "Question Forms": "Questions are formed using question words like Who, What, Where, When, Why, How. Example Tamil: என்ன (enna) = what, எங்கே (enge) = where, எப்போது (eppodu) = when.",
}

QUIZ_DATA = {
    "Kannada": [
        {"question": "What is 'Hello' in Kannada?", "answer": "ನಮಸ್ಕಾರ", "hint": "Namaskara"},
        {"question": "What is 'Water' in Kannada?", "answer": "ನೀರು", "hint": "Neeru"},
        {"question": "What is 'Mother' in Kannada?", "answer": "ತಾಯಿ", "hint": "Taayi"},
        {"question": "What does 'ಪುಸ್ತಕ' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Kannada?", "answer": "ಧನ್ಯವಾದ", "hint": "Dhanyavada"},
        {"question": "What does 'ಪ್ರೀತಿ' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Kannada?", "answer": "ಶಾಲೆ", "hint": "Shaale"},
        {"question": "What is the Kannada word for 'Name'?", "answer": "ಹೆಸರು", "hint": "Hesaru"},
    ],
    "Hindi": [
        {"question": "What is 'Hello' in Hindi?", "answer": "नमस्ते", "hint": "Namaste"},
        {"question": "What is 'Water' in Hindi?", "answer": "पानी", "hint": "Paani"},
        {"question": "What is 'Mother' in Hindi?", "answer": "माँ", "hint": "Maa"},
        {"question": "What does 'किताब' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Hindi?", "answer": "धन्यवाद", "hint": "Dhanyavaad"},
        {"question": "What does 'प्यार' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Hindi?", "answer": "स्कूल", "hint": "Skool"},
        {"question": "What is the Hindi word for 'Name'?", "answer": "नाम", "hint": "Naam"},
    ],
    "Tamil": [
        {"question": "What is 'Hello' in Tamil?", "answer": "வணக்கம்", "hint": "Vanakkam"},
        {"question": "What is 'Water' in Tamil?", "answer": "தண்ணீர்", "hint": "Thanneer"},
        {"question": "What is 'Mother' in Tamil?", "answer": "அம்மா", "hint": "Amma"},
        {"question": "What does 'புத்தகம்' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Tamil?", "answer": "நன்றி", "hint": "Nandri"},
        {"question": "What does 'அன்பு' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Tamil?", "answer": "பள்ளி", "hint": "Palli"},
        {"question": "What is the Tamil word for 'Name'?", "answer": "பெயர்", "hint": "Peyar"},
    ],
    "Telugu": [
        {"question": "What is 'Hello' in Telugu?", "answer": "నమస్కారం", "hint": "Namaskaram"},
        {"question": "What is 'Water' in Telugu?", "answer": "నీరు", "hint": "Neeru"},
        {"question": "What is 'Mother' in Telugu?", "answer": "అమ్మ", "hint": "Amma"},
        {"question": "What does 'పుస్తకం' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Telugu?", "answer": "ధన్యవాదాలు", "hint": "Dhanyavadaalu"},
        {"question": "What does 'ప్రేమ' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Telugu?", "answer": "పాఠశాల", "hint": "Paathashaala"},
        {"question": "What is the Telugu word for 'Name'?", "answer": "పేరు", "hint": "Peru"},
    ],
    "Malayalam": [
        {"question": "What is 'Hello' in Malayalam?", "answer": "നമസ്കാരം", "hint": "Namaskaram"},
        {"question": "What is 'Water' in Malayalam?", "answer": "വെള്ളം", "hint": "Vellam"},
        {"question": "What is 'Mother' in Malayalam?", "answer": "അമ്മ", "hint": "Amma"},
        {"question": "What does 'പുസ്തകം' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Malayalam?", "answer": "നന്ദി", "hint": "Nandi"},
        {"question": "What does 'സ്നേഹം' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Malayalam?", "answer": "വിദ്യാലയം", "hint": "Vidyaalayam"},
        {"question": "What is the Malayalam word for 'Name'?", "answer": "പേര്", "hint": "Per"},
    ],
    "Marathi": [
        {"question": "What is 'Hello' in Marathi?", "answer": "नमस्कार", "hint": "Namaskar"},
        {"question": "What is 'Water' in Marathi?", "answer": "पाणी", "hint": "Paani"},
        {"question": "What is 'Mother' in Marathi?", "answer": "आई", "hint": "Aai"},
        {"question": "What does 'पुस्तक' mean in English?", "answer": "Book", "hint": "Something you read"},
        {"question": "What is 'Thank You' in Marathi?", "answer": "धन्यवाद", "hint": "Dhanyavaad"},
        {"question": "What does 'प्रेम' mean in English?", "answer": "Love", "hint": "A deep feeling"},
        {"question": "What is 'School' in Marathi?", "answer": "शाळा", "hint": "Shaala"},
        {"question": "What is the Marathi word for 'Name'?", "answer": "नाव", "hint": "Naav"},
    ],
}


# --------------------------------------------------
# PUBLIC FUNCTIONS
# --------------------------------------------------

def generate_response(prompt: str, language: str) -> str:
    """
    Generate an AI response using Gemini, tuned for language-learning context.
    Falls back to rule-based responses if Gemini is unavailable.
    """
    system_context = (
        f"You are a friendly and encouraging AI language-learning tutor. "
        f"The student is currently learning {language}. "
        f"When the user asks about words, phrases, grammar, or translation, "
        f"provide helpful, concise explanations with examples in both English and {language}. "
        f"Include pronunciation guides where helpful. "
        f"If the user greets you, greet them warmly in both English and {language}. "
        f"Keep your answers clear, educational, and encouraging. "
        f"Format your response in a readable way."
    )
    full_prompt = f"{system_context}\n\nStudent: {prompt}\n\nTutor:"
    result = _ask_gemini(full_prompt)
    if result and not result.startswith("AI"):
        return result

    # Simple fallback
    p = prompt.lower()
    if any(w in p for w in ["hello", "hi", "hey"]):
        return f"Hello! 👋 I'm here to help you learn {language}. What would you like to know?"
    if "thank" in p:
        return "You're welcome! Keep up the great learning! 🌟"
    if "bye" in p:
        return "Goodbye! Practice every day – consistency is key! 👋"
    return (
        f"Great question! I'll help you learn {language}. "
        f"Try asking me to translate a word, explain grammar, or quiz you on vocabulary!"
    )


def vocabulary_words(language: str) -> list:
    """
    Return a rich vocabulary list for the selected language using Gemini.
    Falls back to static data if Gemini is unavailable.
    """
    prompt = (
        f"Generate a vocabulary list of exactly 15 common {language} words that a beginner should learn. "
        f"Return ONLY a valid JSON array with no markdown, no explanation, no code block. "
        f'Each item must have exactly these keys: "english", "local", "pronunciation", "example_english", "example_local". '
        f"Example of expected format:\n"
        f'[{{"english":"Hello","local":"ನಮಸ್ಕಾರ","pronunciation":"Namaskara","example_english":"Hello, how are you?","example_local":"ನಮಸ್ಕಾರ, ಹೇಗಿದ್ದೀರಿ?"}}]\n'
        f"Generate 15 items in this exact format for {language}."
    )
    raw = _ask_gemini(prompt)
    try:
        # Strip markdown code fences if present
        clean = re.sub(r"```[a-z]*\n?", "", raw).strip().rstrip("`").strip()
        # Find JSON array
        start = clean.find("[")
        end = clean.rfind("]") + 1
        if start != -1 and end > start:
            data = json.loads(clean[start:end])
            if isinstance(data, list) and data:
                return data
    except Exception:
        pass

    # Fallback to static data
    fallback = VOCAB_DATA.get(language, [])
    return [
        {
            "english": eng,
            "local": loc,
            "pronunciation": "",
            "example_english": "",
            "example_local": "",
        }
        for eng, loc in fallback
    ]


def grammar_topics() -> list:
    """Return the list of grammar topics."""
    return list(GRAMMAR_DATA.keys())


def grammar_lesson(topic: str, language: str) -> str:
    """
    Return a detailed grammar lesson for the topic in the selected language.
    Uses Gemini for rich, language-specific content.
    """
    prompt = (
        f"Explain the grammar concept of '{topic}' for someone learning {language}. "
        f"Structure your response as follows:\n"
        f"1. Brief definition (2 sentences)\n"
        f"2. How it works specifically in {language} (3-4 sentences)\n"
        f"3. Three concrete examples with English translation and {language} script\n"
        f"4. One simple tip to remember this rule\n"
        f"Keep the total response under 300 words. Be clear, practical, and beginner-friendly."
    )
    result = _ask_gemini(prompt)
    if result and not result.startswith("AI"):
        return result
    # Fallback
    return GRAMMAR_DATA.get(topic, f"Lesson on {topic} in {language} coming soon.")


def quiz_question(language: str) -> dict:
    """
    Return a quiz question dict with keys: question, answer, hint, options.
    Tries Gemini first for variety, falls back to static data.
    """
    prompt = (
        f"Create one multiple-choice quiz question to test knowledge of {language} vocabulary or grammar. "
        f"Return ONLY valid JSON with no markdown, no code block, no explanation. "
        f'The JSON must have these exact keys: "question", "answer", "hint", "options". '
        f'"options" must be a list of exactly 4 strings (one of which is the correct answer). '
        f'"answer" must exactly match one of the options strings. '
        f"Example format:\n"
        f'{{"question":"What is Hello in {language}?","answer":"CorrectWord","hint":"A greeting","options":["CorrectWord","Wrong1","Wrong2","Wrong3"]}}\n'
        f"Create a new unique question in this format."
    )
    raw = _ask_gemini(prompt)
    try:
        clean = re.sub(r"```[a-z]*\n?", "", raw).strip().rstrip("`").strip()
        start = clean.find("{")
        end = clean.rfind("}") + 1
        if start != -1 and end > start:
            data = json.loads(clean[start:end])
            if all(k in data for k in ("question", "answer", "hint", "options")):
                if isinstance(data["options"], list) and len(data["options"]) == 4:
                    if data["answer"] in data["options"]:
                        random.shuffle(data["options"])
                        return data
    except Exception:
        pass

    # Fallback to static data
    pool = QUIZ_DATA.get(language, QUIZ_DATA["Hindi"])
    q = random.choice(pool).copy()
    # Build fake options from other words
    all_answers = [item["answer"] for item in pool if item["answer"] != q["answer"]]
    distractors = random.sample(all_answers, min(3, len(all_answers)))
    options = distractors + [q["answer"]]
    random.shuffle(options)
    q["options"] = options
    return q


def answer_question(question: str, language: str) -> str:
    """
    Answer any free-form question from the search bar using Gemini.
    Returns a detailed, helpful answer.
    """
    prompt = (
        f"You are a language-learning expert specializing in Indian languages. "
        f"The student is learning {language}. "
        f"Answer the following question in a clear, helpful, and educational way. "
        f"Include examples in both English and {language} where relevant. "
        f"If the question is about a word or phrase, always give the {language} equivalent with pronunciation. "
        f"Keep your response concise (under 200 words) but complete.\n\n"
        f"Question: {question}"
    )
    result = _ask_gemini(prompt)
    if result and not result.startswith("AI"):
        return result
    return (
        f"I'm unable to answer right now (AI unavailable). "
        f"Try asking: 'How do I say X in {language}?' or 'What does Y mean?'"
    )