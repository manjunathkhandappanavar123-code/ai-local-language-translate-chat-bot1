import io
import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

# AI functions
from model import (
    generate_response,
    vocabulary_words,
    grammar_topics,
    grammar_lesson,
    quiz_question,
    answer_question,
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Local Language Learning AI",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Vocab card */
.vocab-card {
    background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8e 100%);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    border-left: 4px solid #4fc3f7;
    transition: transform 0.2s ease;
}
.vocab-card:hover { transform: translateX(4px); }
.vocab-english { font-size: 18px; font-weight: 600; color: #ffffff; }
.vocab-local   { font-size: 20px; font-weight: 700; color: #4fc3f7; }
.vocab-pronun  { font-size: 12px; color: #a0c4e8; font-style: italic; }
.vocab-example { font-size: 13px; color: #c8e0f4; margin-top: 4px; }

/* Option button styling */
div[data-testid="stButton"] button {
    border-radius: 8px;
    font-size: 15px;
    padding: 10px 16px;
    transition: all 0.2s ease;
}

/* Search bar container */
.search-container {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(180deg, transparent 0%, #0e1117 30%);
    padding: 16px 24px 24px;
    z-index: 999;
}

/* Grammar lesson box */
.lesson-box {
    background: #1a2332;
    border: 1px solid #2d4a6e;
    border-radius: 12px;
    padding: 20px;
    line-height: 1.7;
    font-size: 15px;
}

/* Score badge */
.score-badge {
    background: linear-gradient(135deg, #1565C0, #0D47A1);
    color: white;
    border-radius: 20px;
    padding: 6px 18px;
    font-weight: 700;
    font-size: 18px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LANGUAGE SETTINGS
# --------------------------------------------------

LANGUAGES = {
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Marathi": "mr",
}

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

def _init_state():
    defaults = {
        "messages": [],
        "score": 0,
        "language": "Kannada",
        "last_question": None,
        "quiz_answered": False,
        "quiz_result": None,
        "show_hint": False,
        "vocab_cache": {},
        "grammar_cache": {},
        "search_answer": None,
        "search_query": "",
        "quiz_asked_ids": [],
        "last_original": "",
        "last_translated": "",
        "last_trans_lang": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_init_state()

# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def translate_sentence(text: str, target_language: str) -> str:
    """Translate using Google Translate via deep-translator."""
    if not text or not text.strip():
        return ""
    target_code = LANGUAGES[target_language]
    try:
        translator = GoogleTranslator(source="auto", target=target_code)
        return translator.translate(text)
    except Exception as e:
        return f"Translation error: {str(e)}"


def speak_text(text: str, lang_code: str) -> bytes:
    """Convert text to speech using gTTS and return audio bytes."""
    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer.read()
    except Exception as e:
        return None


def get_vocab(language: str):
    if language not in st.session_state.vocab_cache:
        with st.spinner("🤖 Loading vocabulary with AI..."):
            st.session_state.vocab_cache[language] = vocabulary_words(language)
    return st.session_state.vocab_cache[language]


def get_grammar_lesson(topic: str, language: str) -> str:
    key = f"{language}_{topic}"
    if key not in st.session_state.grammar_cache:
        with st.spinner("🤖 Generating lesson with AI..."):
            st.session_state.grammar_cache[key] = grammar_lesson(topic, language)
    return st.session_state.grammar_cache[key]

# --------------------------------------------------
# TITLE & SIDEBAR
# --------------------------------------------------

st.title("🌍 Local Language Learning AI")
st.caption("Learn Indian local languages with AI • Powered by Google Gemini")

st.sidebar.title("📚 Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["🤖 AI Chat", "🌐 Translator", "📖 Vocabulary", "📚 Grammar", "🧠 Quiz", "📊 Progress", "ℹ️ About"],
)

language = st.sidebar.selectbox(
    "🌐 Choose Native Language",
    list(LANGUAGES.keys()),
    index=list(LANGUAGES.keys()).index(st.session_state.language),
)

# Reset caches if language changed
if language != st.session_state.language:
    st.session_state.language = language
    st.session_state.last_question = None
    st.session_state.quiz_answered = False
    st.session_state.quiz_result = None
    st.session_state.show_hint = False

st.sidebar.markdown("---")
st.sidebar.success(f"🗣️ Learning: **{language}**")
st.sidebar.markdown(f"🏆 Quiz Score: **{st.session_state.score}**")

# ==================================================
# AI CHAT
# ==================================================

if page == "🤖 AI Chat":

    st.header("🤖 AI Language Chat")
    st.write(f"Chat with the AI tutor and learn **{language}**.")

    # Display previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask anything about language learning...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("🤔 Thinking..."):
            try:
                answer = generate_response(user_input, language)
            except Exception as e:
                answer = f"AI response failed: {str(e)}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

    if st.session_state.messages:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()


# ==================================================
# TRANSLATOR
# ==================================================

elif page == "🌐 Translator":

    st.header("🌐 Google Sentence Translator")
    st.write(
        "Enter a sentence or paragraph in any language. "
        "The app will automatically detect the source language "
        f"and translate it into **{language}**."
    )

    st.info(f"🎯 Target Language: **{language}**")

    text = st.text_area(
        "✍️ Enter your text",
        height=180,
        placeholder=(
            "Example:\n"
            "I am going to college today.\n\n"
            "You can enter a complete sentence or paragraph."
        ),
    )

    if st.button(f"🔄 Translate to {language}", use_container_width=True):
        if not text.strip():
            st.warning("Please enter some text first.")
        else:
            with st.spinner(f"Translating to {language}..."):
                translated = translate_sentence(text, language)

            if "Translation error" in translated:
                st.error(translated)
            else:
                st.session_state["last_original"] = text
                st.session_state["last_translated"] = translated
                st.session_state["last_trans_lang"] = language

    # Display result if available
    if st.session_state.get("last_translated"):
        orig   = st.session_state["last_original"]
        trans  = st.session_state["last_translated"]
        t_lang = st.session_state.get("last_trans_lang", language)
        t_code = LANGUAGES.get(t_lang, "kn")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📝 Original")
            st.info(orig)
            # Speak original (auto-detect = English fallback)
            if st.button("🔊 Speak Original", key="speak_orig", use_container_width=True):
                with st.spinner("Generating speech..."):
                    audio = speak_text(orig, "en")
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)
                else:
                    st.warning("Could not generate speech for the original text.")

        with col2:
            st.subheader(f"✅ {t_lang} Translation")
            st.success(trans)
            # Speak translated output in the target language
            if st.button(f"🔊 Speak in {t_lang}", key="speak_trans", use_container_width=True):
                with st.spinner(f"Generating {t_lang} speech..."):
                    audio = speak_text(trans, t_code)
                if audio:
                    st.audio(audio, format="audio/mp3", autoplay=True)
                else:
                    st.warning(f"Could not generate speech for {t_lang}.")


# ==================================================
# VOCABULARY
# ==================================================

elif page == "📖 Vocabulary":

    st.header("📖 Daily Vocabulary")
    st.write(f"Learn common **{language}** words with pronunciation and examples.")

    col_refresh, col_info = st.columns([1, 3])
    with col_refresh:
        if st.button("🔄 Refresh Words", use_container_width=True):
            if language in st.session_state.vocab_cache:
                del st.session_state.vocab_cache[language]
            st.rerun()

    words = get_vocab(language)

    if not words:
        st.warning("No vocabulary words available. Try refreshing.")
    else:
        st.markdown(f"**{len(words)} words loaded for {language}** — click 'Refresh Words' to get a new set!")
        st.markdown("---")

        for i, item in enumerate(words):
            english = item.get("english", "")
            local = item.get("local", "")
            pronun = item.get("pronunciation", "")
            ex_en = item.get("example_english", "")
            ex_loc = item.get("example_local", "")

            pronun_html = f'<div class="vocab-pronun">🔊 {pronun}</div>' if pronun else ""
            ex_html = ""
            if ex_en:
                ex_html = (
                    f'<div class="vocab-example">📖 "{ex_en}"</div>'
                    f'<div class="vocab-example">📖 "{ex_loc}"</div>'
                )

            st.markdown(
                f"""
                <div class="vocab-card">
                    <div>
                        <div class="vocab-english">{i+1}. {english}</div>
                        {pronun_html}
                        {ex_html}
                    </div>
                    <div class="vocab-local">{local}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br><br>", unsafe_allow_html=True)


# ==================================================
# GRAMMAR
# ==================================================

elif page == "📚 Grammar":

    st.header("📚 Grammar Lessons")
    st.write(f"Learn **{language}** grammar with AI-powered explanations and examples.")

    topics = grammar_topics()

    if not topics:
        st.warning("No grammar topics available.")
    else:
        # Topic selector with icons
        topic_icons = {
            "Nouns": "🏷️", "Pronouns": "👤", "Verbs": "⚡",
            "Adjectives": "🎨", "Adverbs": "🚀", "Tenses": "⏰",
            "Sentence Formation": "📝", "Question Forms": "❓",
        }

        cols = st.columns(4)
        for i, t in enumerate(topics):
            icon = topic_icons.get(t, "📌")
            with cols[i % 4]:
                if st.button(f"{icon} {t}", key=f"topic_{t}", use_container_width=True):
                    st.session_state["selected_topic"] = t

        selected_topic = st.session_state.get("selected_topic", topics[0])

        st.markdown("---")
        st.subheader(f"📘 {topic_icons.get(selected_topic, '📌')} {selected_topic}")
        st.caption(f"Learning this concept in **{language}**")

        lesson_text = get_grammar_lesson(selected_topic, language)
        st.markdown(
            f'<div class="lesson-box">{lesson_text}</div>',
            unsafe_allow_html=True,
        )

        # Quick practice suggestion
        st.markdown("---")
        st.info(
            f"💡 **Practice Tip:** Go to the **Quiz** page to test your knowledge of {selected_topic} in {language}!"
        )


# ==================================================
# QUIZ
# ==================================================

elif page == "🧠 Quiz":

    st.header("🧠 Language Quiz")
    st.write(f"Test your **{language}** knowledge with multiple-choice questions!")

    # Score display
    score_col, _, skip_col = st.columns([1, 2, 1])
    with score_col:
        st.markdown(
            f'<div class="score-badge">🏆 Score: {st.session_state.score}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Generate question if needed
    if st.session_state.last_question is None:
        st.session_state.quiz_answered = False
        st.session_state.quiz_result = None
        st.session_state.show_hint = False
        try:
            with st.spinner("🤖 Generating a question..."):
                st.session_state.last_question = quiz_question(language)
        except Exception as e:
            st.error(f"Quiz error: {e}")

    question = st.session_state.last_question

    if question:
        q_text = question.get("question", "Question unavailable")
        correct = str(question.get("answer", "")).strip()
        hint = question.get("hint", "")
        options = question.get("options", [])

        st.subheader(f"❓ {q_text}")

        # Hint toggle
        if hint and not st.session_state.quiz_answered:
            if st.button("💡 Show Hint"):
                st.session_state.show_hint = not st.session_state.show_hint

        if st.session_state.show_hint and hint:
            st.info(f"💡 Hint: {hint}")

        st.markdown("**Choose your answer:**")

        if options:
            # Multiple choice buttons (only active before answering)
            cols = st.columns(2)
            for i, opt in enumerate(options):
                with cols[i % 2]:
                    btn_label = opt
                    if st.session_state.quiz_answered:
                        if opt == correct:
                            btn_label = f"✅ {opt}"
                        elif opt == st.session_state.quiz_result and opt != correct:
                            btn_label = f"❌ {opt}"

                    if st.button(btn_label, key=f"opt_{i}_{opt}", use_container_width=True,
                                 disabled=st.session_state.quiz_answered):
                        st.session_state.quiz_answered = True
                        st.session_state.quiz_result = opt
                        if opt.strip().lower() == correct.strip().lower():
                            st.session_state.score += 1
                        st.rerun()

        else:
            # Text input fallback (case-insensitive)
            user_ans = st.text_input("✍️ Your Answer", key="quiz_text_input",
                                     disabled=st.session_state.quiz_answered)
            if st.button("✅ Submit Answer", disabled=st.session_state.quiz_answered or not user_ans):
                st.session_state.quiz_answered = True
                st.session_state.quiz_result = user_ans
                if user_ans.strip().lower() == correct.strip().lower():
                    st.session_state.score += 1
                st.rerun()

        # Show result feedback
        if st.session_state.quiz_answered:
            user_choice = st.session_state.quiz_result or ""
            if user_choice.strip().lower() == correct.strip().lower():
                st.success("🎉 Correct! Well done!")
                st.balloons()
            else:
                st.error(f"❌ Wrong! The correct answer is: **{correct}**")

            st.markdown("---")
            if st.button("➡️ Next Question", use_container_width=True, type="primary"):
                st.session_state.last_question = None
                st.session_state.quiz_answered = False
                st.session_state.quiz_result = None
                st.session_state.show_hint = False
                st.rerun()


# ==================================================
# PROGRESS
# ==================================================

elif page == "📊 Progress":

    st.header("📊 Learning Progress")

    score = st.session_state.score

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Quiz Score", score)
    with col2:
        st.metric("🌐 Language", language)
    with col3:
        st.metric("💬 Chat Messages", len(st.session_state.messages))

    st.markdown("---")

    progress = min(score / 10, 1.0)
    st.subheader("📈 Progress to Level 1 (10 points)")
    st.progress(progress)
    st.write(f"**{score} / 10 points** to complete Level 1")

    if score >= 10:
        st.success("🎉 Excellent! You completed Level 1! Keep going!")
        st.balloons()
    elif score >= 5:
        st.info("👍 Great progress! Halfway there, keep learning!")
    elif score > 0:
        st.warning("📚 Good start! Keep practicing to improve your score.")
    else:
        st.warning("🎯 Take the quiz to start earning points!")

    st.markdown("---")
    if st.button("🔄 Reset Score", type="secondary"):
        st.session_state.score = 0
        st.rerun()


# ==================================================
# ABOUT
# ==================================================

else:

    st.header("ℹ️ About")

    st.write("""
    ### 🌍 Local Language Learning AI

    This application helps users learn Indian local languages using **Google Gemini AI**
    and **Google Translate**.

    ### ✨ Features

    | Feature | Description |
    |---|---|
    | 🤖 AI Chat | Conversational AI tutor powered by Gemini |
    | 🌐 Translator | Full sentence translation via Google Translate |
    | 📖 Vocabulary | AI-generated vocabulary with pronunciation & examples |
    | 📚 Grammar | AI-powered grammar lessons per topic |
    | 🧠 Quiz | Multiple-choice quiz with hints & score tracking |
    | 📊 Progress | Track your learning journey |
    | 🔍 Search Bar | Ask any language question from any page |

    ### 🌐 Supported Languages
    Kannada • Hindi • Tamil • Telugu • Malayalam • Marathi

    ### 🛠️ Technology
    - **AI**: Google Gemini 1.5 Flash
    - **Translation**: Google Translate (deep-translator)
    - **UI**: Streamlit
    """)

    st.success("🌐 Internet connection is required for AI features and translation.")


# ==================================================
# SEARCH BAR  –  Fixed at the bottom of every page
# ==================================================

st.markdown("---")

st.subheader("🔍 Quick Question Search")
st.caption("Ask any language question and get an instant AI answer!")

search_col, btn_col = st.columns([5, 1])

with search_col:
    search_query = st.text_input(
        label="Search / Ask a question",
        placeholder=f"e.g. How do I say 'I am hungry' in {language}? What are common greetings?",
        label_visibility="collapsed",
        key="search_input",
    )

with btn_col:
    search_btn = st.button("🔍 Ask", use_container_width=True, type="primary")

if search_btn and search_query.strip():
    st.session_state.search_query = search_query.strip()
    with st.spinner("🤖 Finding answer..."):
        st.session_state.search_answer = answer_question(
            st.session_state.search_query, language
        )

if st.session_state.search_answer:
    with st.container():
        st.markdown(f"**🔎 Q: {st.session_state.search_query}**")
        st.success(st.session_state.search_answer)
        if st.button("✖️ Clear Answer", key="clear_search"):
            st.session_state.search_answer = None
            st.session_state.search_query = ""
            st.rerun()