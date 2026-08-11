# quiz_data.py
# 500+ quiz questions across 6 Indian languages
# Difficulty: Beginner to Intermediate-Advanced
# Categories: Vocabulary, Grammar, Numbers, Colors, Body Parts,
#             Food, Family, Proverbs, Sentence Structure, Cultural

QUIZ_DB = {

    # ==================================================
    # KANNADA  (~90 questions)
    # ==================================================
    "Kannada": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Kannada?", "answer": "ಚಿಟ್ಟೆ", "hint": "Chitte", "options": ["ಚಿಟ್ಟೆ", "ಹಕ್ಕಿ", "ಮೀನು", "ಹೂ"]},
        {"question": "What is 'Rainbow' in Kannada?", "answer": "ಕಾಮನಬಿಲ್ಲು", "hint": "Kaamanabillu", "options": ["ಕಾಮನಬಿಲ್ಲು", "ಮೋಡ", "ಮಳೆ", "ಬಿಸಿಲು"]},
        {"question": "What is 'Elephant' in Kannada?", "answer": "ಆನೆ", "hint": "Aane", "options": ["ಆನೆ", "ಸಿಂಹ", "ಹುಲಿ", "ಕರಡಿ"]},
        {"question": "What is 'Mountain' in Kannada?", "answer": "ಬೆಟ್ಟ", "hint": "Betta", "options": ["ಬೆಟ್ಟ", "ನದಿ", "ಸಮುದ್ರ", "ಕಾಡು"]},
        {"question": "What is 'Friendship' in Kannada?", "answer": "ಸ್ನೇಹ", "hint": "Sneha", "options": ["ಸ್ನೇಹ", "ಪ್ರೀತಿ", "ಕೋಪ", "ದ್ವೇಷ"]},
        {"question": "What is 'Doctor' in Kannada?", "answer": "ವೈದ್ಯ", "hint": "Vaidya", "options": ["ವೈದ್ಯ", "ಶಿಕ್ಷಕ", "ಪೋಲೀಸ", "ರೈತ"]},
        {"question": "What is 'River' in Kannada?", "answer": "ನದಿ", "hint": "Nadi", "options": ["ನದಿ", "ಕೆರೆ", "ಸಮುದ್ರ", "ಬಾವಿ"]},
        {"question": "What is 'Moon' in Kannada?", "answer": "ಚಂದ್ರ", "hint": "Chandra", "options": ["ಚಂದ್ರ", "ಸೂರ್ಯ", "ನಕ್ಷತ್ರ", "ಆಕಾಶ"]},
        {"question": "What is 'Sun' in Kannada?", "answer": "ಸೂರ್ಯ", "hint": "Soorya", "options": ["ಸೂರ್ಯ", "ಚಂದ್ರ", "ನಕ್ಷತ್ರ", "ಮೋಡ"]},
        {"question": "What is 'Wind' in Kannada?", "answer": "ಗಾಳಿ", "hint": "Gaali", "options": ["ಗಾಳಿ", "ನೀರು", "ಬೆಂಕಿ", "ಮಣ್ಣು"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Kannada?", "answer": "ಏಳು", "hint": "Elu", "options": ["ಏಳು", "ಆರು", "ಎಂಟು", "ಒಂಬತ್ತು"]},
        {"question": "What is 'Twelve' in Kannada?", "answer": "ಹನ್ನೆರಡು", "hint": "Hanneradu", "options": ["ಹನ್ನೆರಡು", "ಹತ್ತು", "ಹದಿನೈದು", "ಇಪ್ಪತ್ತು"]},
        {"question": "What is 'Fifty' in Kannada?", "answer": "ಐವತ್ತು", "hint": "Aivattu", "options": ["ಐವತ್ತು", "ನಲವತ್ತು", "ಅರವತ್ತು", "ಎಪ್ಪತ್ತು"]},
        {"question": "What is 'Hundred' in Kannada?", "answer": "ನೂರು", "hint": "Nooru", "options": ["ನೂರು", "ಸಾವಿರ", "ಐದು", "ಎಪ್ಪತ್ತು"]},
        {"question": "What is 'Zero' in Kannada?", "answer": "ಸೊನ್ನೆ", "hint": "Sonne", "options": ["ಸೊನ್ನೆ", "ಒಂದು", "ಎರಡು", "ಮೂರು"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Kannada?", "answer": "ನೇರಳೆ", "hint": "Nerale", "options": ["ನೇರಳೆ", "ಹಸಿರು", "ನೀಲಿ", "ಕೆಂಪು"]},
        {"question": "What is 'Orange' in Kannada?", "answer": "ಕಿತ್ತಳೆ ಬಣ್ಣ", "hint": "Kittale banna", "options": ["ಕಿತ್ತಳೆ ಬಣ್ಣ", "ಹಳದಿ", "ಕೆಂಪು", "ಗುಲಾಬಿ"]},
        {"question": "What is 'Brown' in Kannada?", "answer": "ಕಂದು", "hint": "Kandu", "options": ["ಕಂದು", "ಬಿಳಿ", "ಕಪ್ಪು", "ಬೂದು"]},
        {"question": "What is 'Pink' in Kannada?", "answer": "ಗುಲಾಬಿ", "hint": "Gulaabi", "options": ["ಗುಲಾಬಿ", "ಹಸಿರು", "ನೀಲಿ", "ಕಂದು"]},
        {"question": "What is 'Silver' in Kannada?", "answer": "ಬೆಳ್ಳಿ ಬಣ್ಣ", "hint": "Belli banna", "options": ["ಬೆಳ್ಳಿ ಬಣ್ಣ", "ಚಿನ್ನದ ಬಣ್ಣ", "ಕಪ್ಪು", "ಬಿಳಿ"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Kannada?", "answer": "ಭುಜ", "hint": "Bhuja", "options": ["ಭುಜ", "ಮೊಣಕೈ", "ಮಂಡಿ", "ಮಣಕಾಲು"]},
        {"question": "What is 'Forehead' in Kannada?", "answer": "ಹಣೆ", "hint": "Hane", "options": ["ಹಣೆ", "ಕಣ್ಣು", "ಮೂಗು", "ತಲೆ"]},
        {"question": "What is 'Chin' in Kannada?", "answer": "ಗದ್ದ", "hint": "Gadda", "options": ["ಗದ್ದ", "ಕೆನ್ನೆ", "ಹಣೆ", "ತುಟಿ"]},
        {"question": "What is 'Thumb' in Kannada?", "answer": "ಹೆಬ್ಬೆರಳು", "hint": "Hebberalu", "options": ["ಹೆಬ್ಬೆರಳು", "ಬೆರಳು", "ಕೈ", "ಮಣಿಕಟ್ಟು"]},
        {"question": "What is 'Knee' in Kannada?", "answer": "ಮಂಡಿ", "hint": "Mandi", "options": ["ಮಂಡಿ", "ಕಾಲು", "ಮಣಕಾಲು", "ತೊಡೆ"]},
        # --- Food ---
        {"question": "What is 'Rice' in Kannada?", "answer": "ಅನ್ನ", "hint": "Anna", "options": ["ಅನ್ನ", "ರೊಟ್ಟಿ", "ಸಂಬಾರ", "ಉಪ್ಪಿಟ್ಟು"]},
        {"question": "What is 'Milk' in Kannada?", "answer": "ಹಾಲು", "hint": "Haalu", "options": ["ಹಾಲು", "ನೀರು", "ಜ್ಯೂಸ್", "ಚಹಾ"]},
        {"question": "What is 'Salt' in Kannada?", "answer": "ಉಪ್ಪು", "hint": "Uppu", "options": ["ಉಪ್ಪು", "ಸಕ್ಕರೆ", "ಖಾರ", "ಹುಳಿ"]},
        {"question": "What is 'Mango' in Kannada?", "answer": "ಮಾವಿನ ಹಣ್ಣು", "hint": "Maavina hannu", "options": ["ಮಾವಿನ ಹಣ್ಣು", "ಬಾಳೆ ಹಣ್ಣು", "ದ್ರಾಕ್ಷಿ", "ಸೇಬು"]},
        {"question": "What is 'Onion' in Kannada?", "answer": "ಈರುಳ್ಳಿ", "hint": "Eerulli", "options": ["ಈರುಳ್ಳಿ", "ಟೊಮೆಟೊ", "ಆಲೂಗಡ್ಡೆ", "ಕ್ಯಾರೆಟ್"]},
        # --- Family ---
        {"question": "What is 'Sister' in Kannada?", "answer": "ಅಕ್ಕ / ತಂಗಿ", "hint": "Akka/Tangi", "options": ["ಅಕ್ಕ / ತಂಗಿ", "ಅಣ್ಣ", "ಅಮ್ಮ", "ಅತ್ತೆ"]},
        {"question": "What is 'Grandfather' in Kannada?", "answer": "ತಾತ", "hint": "Taata", "options": ["ತಾತ", "ಅಜ್ಜಿ", "ಅಪ್ಪ", "ಮಾವ"]},
        {"question": "What is 'Uncle' in Kannada?", "answer": "ಚಿಕ್ಕಪ್ಪ / ದೊಡ್ಡಪ್ಪ", "hint": "Chikkappa", "options": ["ಚಿಕ್ಕಪ್ಪ / ದೊಡ್ಡಪ್ಪ", "ಅಣ್ಣ", "ಮಗ", "ತಮ್ಮ"]},
        {"question": "What is 'Daughter' in Kannada?", "answer": "ಮಗಳು", "hint": "Magalu", "options": ["ಮಗಳು", "ಮಗ", "ಅಕ್ಕ", "ಅಮ್ಮ"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Kannada?", "answer": "ನನಗೆ ಹಸಿವು", "hint": "Nanage hasivu", "options": ["ನನಗೆ ಹಸಿವು", "ನನಗೆ ನಿದ್ದೆ", "ನನಗೆ ಬಾಯಾರಿಕೆ", "ನನಗೆ ಜ್ವರ"]},
        {"question": "How do you say 'I am going to school' in Kannada?", "answer": "ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ", "hint": "Naanu shaalege hoguttene", "options": ["ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ", "ನಾನು ಮನೆಗೆ ಹೋಗುತ್ತೇನೆ", "ನಾನು ಓದುತ್ತೇನೆ", "ನಾನು ಬರುತ್ತೇನೆ"]},
        {"question": "What does 'ನಿಮ್ಮ ಹೆಸರೇನು?' mean?", "answer": "What is your name?", "hint": "A question about identity", "options": ["What is your name?", "Where do you live?", "How old are you?", "What do you do?"]},
        {"question": "What does 'ಧನ್ಯವಾದಗಳು' mean?", "answer": "Thank you", "hint": "An expression of gratitude", "options": ["Thank you", "Sorry", "Hello", "Goodbye"]},
        {"question": "What is 'Please' in Kannada?", "answer": "ದಯವಿಟ್ಟು", "hint": "Dayavittu", "options": ["ದಯವಿಟ್ಟು", "ಧನ್ಯವಾದ", "ಕ್ಷಮಿಸಿ", "ನಮಸ್ಕಾರ"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Kannada?", "answer": "ನಾಳೆ", "hint": "Naale", "options": ["ನಾಳೆ", "ನಿನ್ನೆ", "ಇಂದು", "ಮೊನ್ನೆ"]},
        {"question": "What is 'Monday' in Kannada?", "answer": "ಸೋಮವಾರ", "hint": "Somavaara", "options": ["ಸೋಮವಾರ", "ಮಂಗಳವಾರ", "ಶನಿವಾರ", "ಭಾನುವಾರ"]},
        {"question": "What is 'Morning' in Kannada?", "answer": "ಬೆಳಿಗ್ಗೆ", "hint": "Beligge", "options": ["ಬೆಳಿಗ್ಗೆ", "ಮಧ್ಯಾಹ್ನ", "ಸಂಜೆ", "ರಾತ್ರಿ"]},
        {"question": "What is 'Night' in Kannada?", "answer": "ರಾತ್ರಿ", "hint": "Raatri", "options": ["ರಾತ್ರಿ", "ಬೆಳಿಗ್ಗೆ", "ಮಧ್ಯಾಹ್ನ", "ಸಂಜೆ"]},
        {"question": "What is 'Year' in Kannada?", "answer": "ವರ್ಷ", "hint": "Varsha", "options": ["ವರ್ಷ", "ತಿಂಗಳು", "ವಾರ", "ದಿನ"]},
        # --- Places ---
        {"question": "What is 'Hospital' in Kannada?", "answer": "ಆಸ್ಪತ್ರೆ", "hint": "Aaspatre", "options": ["ಆಸ್ಪತ್ರೆ", "ಶಾಲೆ", "ಮಾರುಕಟ್ಟೆ", "ದೇವಾಲಯ"]},
        {"question": "What is 'Market' in Kannada?", "answer": "ಮಾರುಕಟ್ಟೆ", "hint": "Maarukatte", "options": ["ಮಾರುಕಟ್ಟೆ", "ಆಸ್ಪತ್ರೆ", "ಶಾಲೆ", "ಗ್ರಂಥಾಲಯ"]},
        {"question": "What is 'Temple' in Kannada?", "answer": "ದೇವಾಲಯ", "hint": "Devaalaya", "options": ["ದೇವಾಲಯ", "ಮಸೀದಿ", "ಚರ್ಚ್", "ಆಸ್ಪತ್ರೆ"]},
        {"question": "What is 'Library' in Kannada?", "answer": "ಗ್ರಂಥಾಲಯ", "hint": "Granthalaya", "options": ["ಗ್ರಂಥಾಲಯ", "ಶಾಲೆ", "ಕಚೇರಿ", "ಮಾರುಕಟ್ಟೆ"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Kannada?", "answer": "ಗಿಣಿ", "hint": "Gini", "options": ["ಗಿಣಿ", "ಹಕ್ಕಿ", "ಕಾಗೆ", "ಗುಬ್ಬಿ"]},
        {"question": "What is 'Tiger' in Kannada?", "answer": "ಹುಲಿ", "hint": "Huli", "options": ["ಹುಲಿ", "ಚಿರತೆ", "ಸಿಂಹ", "ಕರಡಿ"]},
        {"question": "What is 'Cow' in Kannada?", "answer": "ಹಸು", "hint": "Hasu", "options": ["ಹಸು", "ಎಮ್ಮೆ", "ಮೇಕೆ", "ಕುರಿ"]},
        {"question": "What is 'Horse' in Kannada?", "answer": "ಕುದುರೆ", "hint": "Kudure", "options": ["ಕುದುರೆ", "ಆನೆ", "ಒಂಟೆ", "ಕತ್ತೆ"]},
        {"question": "What is 'Fish' in Kannada?", "answer": "ಮೀನು", "hint": "Meenu", "options": ["ಮೀನು", "ಏಡಿ", "ಕಪ್ಪೆ", "ಆಮೆ"]},
        # --- Adjectives ---
        {"question": "What is 'Beautiful' in Kannada?", "answer": "ಸುಂದರ", "hint": "Sundara", "options": ["ಸುಂದರ", "ಕೊಳಕು", "ವಿಚಿತ್ರ", "ಭಯಂಕರ"]},
        {"question": "What is 'Intelligent' in Kannada?", "answer": "ಬುದ್ಧಿವಂತ", "hint": "Buddhivanta", "options": ["ಬುದ್ಧಿವಂತ", "ಮೂರ್ಖ", "ದಯಾಳು", "ದೊಡ್ಡ"]},
        {"question": "What is 'Brave' in Kannada?", "answer": "ಧೈರ್ಯಶಾಲಿ", "hint": "Dhairyashaali", "options": ["ಧೈರ್ಯಶಾಲಿ", "ಹೇಡಿ", "ಸೋಮಾರಿ", "ದುರಾಶೆ"]},
        {"question": "What is 'Hot' in Kannada?", "answer": "ಬಿಸಿ", "hint": "Bisi", "options": ["ಬಿಸಿ", "ತಣ್ಣನೆ", "ಉಷ್ಣ", "ಮೃದು"]},
        {"question": "What is 'Heavy' in Kannada?", "answer": "ಭಾರ", "hint": "Bhaara", "options": ["ಭಾರ", "ಹಗುರ", "ದೊಡ್ಡ", "ಸಣ್ಣ"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Kannada?", "answer": "ತಿನ್ನು", "hint": "Tinnu", "options": ["ತಿನ್ನು", "ಕುಡಿ", "ಓಡು", "ನಡೆ"]},
        {"question": "What is 'To sleep' in Kannada?", "answer": "ಮಲಗು", "hint": "Malagu", "options": ["ಮಲಗು", "ಎದ್ದೇಳು", "ಕುಳಿತು", "ನಡೆ"]},
        {"question": "What is 'To speak' in Kannada?", "answer": "ಮಾತನಾಡು", "hint": "Maatanaadu", "options": ["ಮಾತನಾಡು", "ಕೇಳು", "ಓದು", "ಬರೆ"]},
        {"question": "What is 'To write' in Kannada?", "answer": "ಬರೆ", "hint": "Bare", "options": ["ಬರೆ", "ಓದು", "ನೋಡು", "ಮಾಡು"]},
        {"question": "What is 'To laugh' in Kannada?", "answer": "ನಗು", "hint": "Nagu", "options": ["ನಗು", "ಅಳು", "ಹಾಡು", "ಕುಣಿ"]},
        # --- Proverbs / Idioms ---
        {"question": "What does 'ಉಪ್ಪು ತಿಂದ ಮನೆ' mean?", "answer": "House that has fed you", "hint": "About loyalty and gratitude", "options": ["House that has fed you", "A salty house", "A poor household", "An old house"]},
        {"question": "Which script is used to write Kannada?", "answer": "Kannada script", "hint": "It is unique to the language", "options": ["Kannada script", "Devanagari", "Tamil script", "Telugu script"]},
        {"question": "Kannada is primarily spoken in which Indian state?", "answer": "Karnataka", "hint": "Garden city is its capital", "options": ["Karnataka", "Tamil Nadu", "Kerala", "Andhra Pradesh"]},
        {"question": "What does 'ಬನ್ನಿ' mean in Kannada?", "answer": "Please come / Welcome", "hint": "An invitation", "options": ["Please come / Welcome", "Go away", "Sit down", "Stand up"]},
        {"question": "What is 'Happiness' in Kannada?", "answer": "ಸಂತೋಷ", "hint": "Santosha", "options": ["ಸಂತೋಷ", "ದುಃಖ", "ಕೋಪ", "ಭಯ"]},
        {"question": "What is 'Sky' in Kannada?", "answer": "ಆಕಾಶ", "hint": "Aakaasha", "options": ["ಆಕಾಶ", "ಭೂಮಿ", "ನೀರು", "ಕಾಡು"]},
        {"question": "What is 'Flower' in Kannada?", "answer": "ಹೂ", "hint": "Hoo", "options": ["ಹೂ", "ಎಲೆ", "ಮರ", "ಬೇರು"]},
        {"question": "What is 'Tree' in Kannada?", "answer": "ಮರ", "hint": "Mara", "options": ["ಮರ", "ಗಿಡ", "ಹೂ", "ಹುಲ್ಲು"]},
        {"question": "What is 'Road' in Kannada?", "answer": "ರಸ್ತೆ", "hint": "Raste", "options": ["ರಸ್ತೆ", "ಸೇತುವೆ", "ಕಾಲ್ದಾರಿ", "ಹೊಲ"]},
        {"question": "What is 'Village' in Kannada?", "answer": "ಹಳ್ಳಿ", "hint": "Halli", "options": ["ಹಳ್ಳಿ", "ನಗರ", "ಶಹರ", "ಜಿಲ್ಲೆ"]},
        {"question": "What is 'City' in Kannada?", "answer": "ನಗರ", "hint": "Nagara", "options": ["ನಗರ", "ಹಳ್ಳಿ", "ದೇಶ", "ರಾಜ್ಯ"]},
        {"question": "What is 'Country' in Kannada?", "answer": "ದೇಶ", "hint": "Desha", "options": ["ದೇಶ", "ರಾಜ್ಯ", "ಜಿಲ್ಲೆ", "ನಗರ"]},
        {"question": "What is 'Rain' in Kannada?", "answer": "ಮಳೆ", "hint": "Male", "options": ["ಮಳೆ", "ಬಿಸಿಲು", "ಗಾಳಿ", "ಮಂಜು"]},
        {"question": "What is 'Star' in Kannada?", "answer": "ನಕ್ಷತ್ರ", "hint": "Nakshatra", "options": ["ನಕ್ಷತ್ರ", "ಚಂದ್ರ", "ಸೂರ್ಯ", "ಮೋಡ"]},
        {"question": "What is 'Cloud' in Kannada?", "answer": "ಮೋಡ", "hint": "Moda", "options": ["ಮೋಡ", "ಗಾಳಿ", "ಮಳೆ", "ಆಕಾಶ"]},
        {"question": "What is 'Gold' in Kannada?", "answer": "ಚಿನ್ನ", "hint": "Chinna", "options": ["ಚಿನ್ನ", "ಬೆಳ್ಳಿ", "ಕಬ್ಬಿಣ", "ತಾಮ್ರ"]},
        {"question": "What is 'King' in Kannada?", "answer": "ರಾಜ", "hint": "Raaja", "options": ["ರಾಜ", "ರಾಣಿ", "ಸೈನಿಕ", "ಮಂತ್ರಿ"]},
        {"question": "What is 'War' in Kannada?", "answer": "ಯುದ್ಧ", "hint": "Yuddha", "options": ["ಯುದ್ಧ", "ಶಾಂತಿ", "ಒಪ್ಪಂದ", "ಆಚರಣೆ"]},
        {"question": "What is 'Victory' in Kannada?", "answer": "ಜಯ", "hint": "Jaya", "options": ["ಜಯ", "ಸೋಲು", "ಹೋರಾಟ", "ಪ್ರಯತ್ನ"]},
        {"question": "What is 'Peace' in Kannada?", "answer": "ಶಾಂತಿ", "hint": "Shaanti", "options": ["ಶಾಂತಿ", "ಯುದ್ಧ", "ಕೋಲಾಹಲ", "ಕೋಪ"]},
        {"question": "What is 'Dream' in Kannada?", "answer": "ಕನಸು", "hint": "Kanasu", "options": ["ಕನಸು", "ನಿದ್ದೆ", "ಆಸೆ", "ನೆನಪು"]},
        {"question": "What is 'Memory' in Kannada?", "answer": "ನೆನಪು", "hint": "Nenapu", "options": ["ನೆನಪು", "ಮರೆವು", "ಕನಸು", "ಭಾವನೆ"]},
        {"question": "What is 'Language' in Kannada?", "answer": "ಭಾಷೆ", "hint": "Bhaashe", "options": ["ಭಾಷೆ", "ಮಾತು", "ಅಕ್ಷರ", "ಪದ"]},
        {"question": "What is 'Teacher' in Kannada?", "answer": "ಶಿಕ್ಷಕ", "hint": "Shikshaka", "options": ["ಶಿಕ್ಷಕ", "ವಿದ್ಯಾರ್ಥಿ", "ವೈದ್ಯ", "ನ್ಯಾಯಾಧೀಶ"]},
        {"question": "What is 'Student' in Kannada?", "answer": "ವಿದ್ಯಾರ್ಥಿ", "hint": "Vidyaarthi", "options": ["ವಿದ್ಯಾರ್ಥಿ", "ಶಿಕ್ಷಕ", "ಮುಖ್ಯಸ್ಥ", "ಗ್ರಂಥಪಾಲ"]},
        {"question": "What is 'Knowledge' in Kannada?", "answer": "ಜ್ಞಾನ", "hint": "Jnaana", "options": ["ಜ್ಞಾನ", "ಅಜ್ಞಾನ", "ವಿದ್ಯೆ", "ಬುದ್ಧಿ"]},
    ],

    # ==================================================
    # HINDI  (~90 questions)
    # ==================================================
    "Hindi": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Hindi?", "answer": "तितली", "hint": "Titli", "options": ["तितली", "पक्षी", "मछली", "फूल"]},
        {"question": "What is 'Rainbow' in Hindi?", "answer": "इंद्रधनुष", "hint": "Indradhanush", "options": ["इंद्रधनुष", "बादल", "बारिश", "धूप"]},
        {"question": "What is 'Elephant' in Hindi?", "answer": "हाथी", "hint": "Haathi", "options": ["हाथी", "शेर", "बाघ", "भालू"]},
        {"question": "What is 'Mountain' in Hindi?", "answer": "पहाड़", "hint": "Pahad", "options": ["पहाड़", "नदी", "समुद्र", "जंगल"]},
        {"question": "What is 'Friendship' in Hindi?", "answer": "दोस्ती", "hint": "Dosti", "options": ["दोस्ती", "प्यार", "गुस्सा", "नफ़रत"]},
        {"question": "What is 'Doctor' in Hindi?", "answer": "डॉक्टर", "hint": "Doctor", "options": ["डॉक्टर", "शिक्षक", "पुलिस", "किसान"]},
        {"question": "What is 'River' in Hindi?", "answer": "नदी", "hint": "Nadi", "options": ["नदी", "तालाब", "समुद्र", "कुआँ"]},
        {"question": "What is 'Moon' in Hindi?", "answer": "चाँद", "hint": "Chaand", "options": ["चाँद", "सूरज", "तारा", "आकाश"]},
        {"question": "What is 'Wind' in Hindi?", "answer": "हवा", "hint": "Hawa", "options": ["हवा", "पानी", "आग", "मिट्टी"]},
        {"question": "What is 'Happiness' in Hindi?", "answer": "खुशी", "hint": "Khushi", "options": ["खुशी", "दुख", "गुस्सा", "डर"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Hindi?", "answer": "सात", "hint": "Saat", "options": ["सात", "छह", "आठ", "नौ"]},
        {"question": "What is 'Eleven' in Hindi?", "answer": "ग्यारह", "hint": "Gyaarah", "options": ["ग्यारह", "दस", "बारह", "पन्द्रह"]},
        {"question": "What is 'Twenty-five' in Hindi?", "answer": "पच्चीस", "hint": "Pachchees", "options": ["पच्चीस", "पंद्रह", "पैंतीस", "पैंतालीस"]},
        {"question": "What is 'Hundred' in Hindi?", "answer": "सौ", "hint": "Sau", "options": ["सौ", "हजार", "पचास", "दस"]},
        {"question": "What is 'Thousand' in Hindi?", "answer": "हजार", "hint": "Hazaar", "options": ["हजार", "सौ", "दस", "लाख"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Hindi?", "answer": "बैंगनी", "hint": "Baingani", "options": ["बैंगनी", "हरा", "नीला", "लाल"]},
        {"question": "What is 'Orange' in Hindi?", "answer": "नारंगी", "hint": "Naarangi", "options": ["नारंगी", "पीला", "लाल", "गुलाबी"]},
        {"question": "What is 'Brown' in Hindi?", "answer": "भूरा", "hint": "Bhoora", "options": ["भूरा", "सफेद", "काला", "स्लेटी"]},
        {"question": "What is 'Pink' in Hindi?", "answer": "गुलाबी", "hint": "Gulaabi", "options": ["गुलाबी", "हरा", "नीला", "भूरा"]},
        {"question": "What is 'Golden' in Hindi?", "answer": "सुनहरा", "hint": "Sunahra", "options": ["सुनहरा", "चाँदी जैसा", "काला", "सफेद"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Hindi?", "answer": "कंधा", "hint": "Kandha", "options": ["कंधा", "कोहनी", "घुटना", "एड़ी"]},
        {"question": "What is 'Forehead' in Hindi?", "answer": "माथा", "hint": "Maathaa", "options": ["माथा", "आँख", "नाक", "सिर"]},
        {"question": "What is 'Chin' in Hindi?", "answer": "ठुड्डी", "hint": "Thuddi", "options": ["ठुड्डी", "गाल", "माथा", "होंठ"]},
        {"question": "What is 'Thumb' in Hindi?", "answer": "अंगूठा", "hint": "Angutha", "options": ["अंगूठा", "उंगली", "हथेली", "कलाई"]},
        {"question": "What is 'Knee' in Hindi?", "answer": "घुटना", "hint": "Ghutna", "options": ["घुटना", "पैर", "जाँघ", "टखना"]},
        # --- Food ---
        {"question": "What is 'Rice' in Hindi?", "answer": "चावल", "hint": "Chaawal", "options": ["चावल", "रोटी", "दाल", "सब्जी"]},
        {"question": "What is 'Bread/Roti' in Hindi?", "answer": "रोटी", "hint": "Roti", "options": ["रोटी", "चावल", "दाल", "चाय"]},
        {"question": "What is 'Salt' in Hindi?", "answer": "नमक", "hint": "Namak", "options": ["नमक", "चीनी", "मिर्च", "हल्दी"]},
        {"question": "What is 'Mango' in Hindi?", "answer": "आम", "hint": "Aam", "options": ["आम", "केला", "अंगूर", "सेब"]},
        {"question": "What is 'Onion' in Hindi?", "answer": "प्याज", "hint": "Pyaaz", "options": ["प्याज", "टमाटर", "आलू", "गाजर"]},
        # --- Family ---
        {"question": "What is 'Sister' in Hindi?", "answer": "बहन", "hint": "Bahan", "options": ["बहन", "भाई", "माँ", "चाची"]},
        {"question": "What is 'Grandfather' in Hindi?", "answer": "दादा", "hint": "Daadaa", "options": ["दादा", "दादी", "पिता", "मामा"]},
        {"question": "What is 'Uncle (father's brother)' in Hindi?", "answer": "चाचा", "hint": "Chaacha", "options": ["चाचा", "मामा", "भाई", "बेटा"]},
        {"question": "What is 'Daughter' in Hindi?", "answer": "बेटी", "hint": "Beti", "options": ["बेटी", "बेटा", "बहन", "माँ"]},
        {"question": "What is 'Husband' in Hindi?", "answer": "पति", "hint": "Pati", "options": ["पति", "पत्नी", "भाई", "पिता"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Hindi?", "answer": "मुझे भूख लगी है", "hint": "Mujhe bhook lagi hai", "options": ["मुझे भूख लगी है", "मुझे नींद आ रही है", "मुझे प्यास लगी है", "मुझे बुखार है"]},
        {"question": "What does 'आप कैसे हैं?' mean?", "answer": "How are you?", "hint": "A greeting question", "options": ["How are you?", "What is your name?", "Where do you live?", "What do you do?"]},
        {"question": "What is 'Please' in Hindi?", "answer": "कृपया", "hint": "Kripaya", "options": ["कृपया", "धन्यवाद", "माफ करना", "नमस्ते"]},
        {"question": "What does 'मेरा नाम राज है' mean?", "answer": "My name is Raj", "hint": "Self-introduction", "options": ["My name is Raj", "His name is Raj", "Your name is Raj", "Her name is Raj"]},
        {"question": "What is 'Sorry' in Hindi?", "answer": "माफ करना", "hint": "Maaf karna", "options": ["माफ करना", "धन्यवाद", "कृपया", "ठीक है"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Hindi?", "answer": "कल", "hint": "Kal (also means yesterday - context-dependent)", "options": ["कल", "परसों", "आज", "अभी"]},
        {"question": "What is 'Monday' in Hindi?", "answer": "सोमवार", "hint": "Somvaar", "options": ["सोमवार", "मंगलवार", "शनिवार", "रविवार"]},
        {"question": "What is 'Morning' in Hindi?", "answer": "सुबह", "hint": "Subah", "options": ["सुबह", "दोपहर", "शाम", "रात"]},
        {"question": "What is 'Year' in Hindi?", "answer": "साल / वर्ष", "hint": "Saal/Varsh", "options": ["साल / वर्ष", "महीना", "हफ्ता", "दिन"]},
        {"question": "What is 'Hour' in Hindi?", "answer": "घंटा", "hint": "Ghanta", "options": ["घंटा", "मिनट", "सेकंड", "दिन"]},
        # --- Places ---
        {"question": "What is 'Hospital' in Hindi?", "answer": "अस्पताल", "hint": "Aspataal", "options": ["अस्पताल", "स्कूल", "बाज़ार", "मंदिर"]},
        {"question": "What is 'Market' in Hindi?", "answer": "बाज़ार", "hint": "Baazaar", "options": ["बाज़ार", "अस्पताल", "स्कूल", "पुस्तकालय"]},
        {"question": "What is 'Temple' in Hindi?", "answer": "मंदिर", "hint": "Mandir", "options": ["मंदिर", "मस्जिद", "गिरजाघर", "अस्पताल"]},
        {"question": "What is 'Airport' in Hindi?", "answer": "हवाई अड्डा", "hint": "Hawai adda", "options": ["हवाई अड्डा", "रेलवे स्टेशन", "बस स्टैंड", "बंदरगाह"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Hindi?", "answer": "तोता", "hint": "Tota", "options": ["तोता", "कौआ", "गौरैया", "मोर"]},
        {"question": "What is 'Peacock' in Hindi?", "answer": "मोर", "hint": "Mor", "options": ["मोर", "तोता", "कबूतर", "बाज"]},
        {"question": "What is 'Cow' in Hindi?", "answer": "गाय", "hint": "Gaay", "options": ["गाय", "भैंस", "बकरी", "भेड़"]},
        {"question": "What is 'Horse' in Hindi?", "answer": "घोड़ा", "hint": "Ghoda", "options": ["घोड़ा", "हाथी", "ऊँट", "गधा"]},
        {"question": "What is 'Crocodile' in Hindi?", "answer": "मगरमच्छ", "hint": "Magarmachh", "options": ["मगरमच्छ", "सांप", "कछुआ", "छिपकली"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Hindi?", "answer": "खाना", "hint": "Khaana", "options": ["खाना", "पीना", "दौड़ना", "चलना"]},
        {"question": "What is 'To sleep' in Hindi?", "answer": "सोना", "hint": "Sona", "options": ["सोना", "उठना", "बैठना", "चलना"]},
        {"question": "What is 'To speak' in Hindi?", "answer": "बोलना", "hint": "Bolna", "options": ["बोलना", "सुनना", "पढ़ना", "लिखना"]},
        {"question": "What is 'To laugh' in Hindi?", "answer": "हँसना", "hint": "Hansna", "options": ["हँसना", "रोना", "गाना", "नाचना"]},
        {"question": "What is 'To think' in Hindi?", "answer": "सोचना", "hint": "Sochna", "options": ["सोचना", "देखना", "सुनना", "महसूस करना"]},
        # --- Adjectives ---
        {"question": "What is 'Beautiful' in Hindi?", "answer": "सुंदर", "hint": "Sundar", "options": ["सुंदर", "बदसूरत", "अजीब", "डरावना"]},
        {"question": "What is 'Brave' in Hindi?", "answer": "बहादुर", "hint": "Bahaadur", "options": ["बहादुर", "डरपोक", "आलसी", "लालची"]},
        {"question": "What is 'Heavy' in Hindi?", "answer": "भारी", "hint": "Bhaari", "options": ["भारी", "हल्का", "बड़ा", "छोटा"]},
        {"question": "What is 'Fast' in Hindi?", "answer": "तेज़", "hint": "Tez", "options": ["तेज़", "धीमा", "लंबा", "छोटा"]},
        {"question": "What is 'Old' in Hindi?", "answer": "बूढ़ा / पुराना", "hint": "Boodha/Puraana", "options": ["बूढ़ा / पुराना", "नया", "जवान", "ताज़ा"]},
        # --- Proverbs / Culture ---
        {"question": "What does 'जैसी करनी वैसी भरनी' mean?", "answer": "As you sow, so shall you reap", "hint": "About consequences of actions", "options": ["As you sow, so shall you reap", "Time is money", "Honesty is best policy", "Blood is thicker than water"]},
        {"question": "Hindi is written in which script?", "answer": "Devanagari", "hint": "Also used for Sanskrit and Marathi", "options": ["Devanagari", "Perso-Arabic", "Latin", "Gurmukhi"]},
        {"question": "Hindi is primarily spoken in which country?", "answer": "India", "hint": "Largest democracy", "options": ["India", "Pakistan", "Nepal", "Bangladesh"]},
        {"question": "What does 'चलो' mean in Hindi?", "answer": "Let's go / Come on", "hint": "Used when leaving", "options": ["Let's go / Come on", "Stop", "Sit down", "Wait"]},
        {"question": "What is 'Rain' in Hindi?", "answer": "बारिश", "hint": "Baarish", "options": ["बारिश", "धूप", "हवा", "बर्फ"]},
        {"question": "What is 'Sky' in Hindi?", "answer": "आसमान", "hint": "Aasmaan", "options": ["आसमान", "धरती", "पानी", "जंगल"]},
        {"question": "What is 'Road' in Hindi?", "answer": "सड़क", "hint": "Sadak", "options": ["सड़क", "पुल", "रास्ता", "खेत"]},
        {"question": "What is 'Village' in Hindi?", "answer": "गाँव", "hint": "Gaanv", "options": ["गाँव", "शहर", "राज्य", "देश"]},
        {"question": "What is 'Dream' in Hindi?", "answer": "सपना", "hint": "Sapna", "options": ["सपना", "नींद", "इच्छा", "यादें"]},
        {"question": "What is 'Knowledge' in Hindi?", "answer": "ज्ञान", "hint": "Gyaan", "options": ["ज्ञान", "अज्ञान", "शिक्षा", "बुद्धि"]},
        {"question": "What is 'Victory' in Hindi?", "answer": "जीत", "hint": "Jeet", "options": ["जीत", "हार", "लड़ाई", "कोशिश"]},
        {"question": "What is 'Peace' in Hindi?", "answer": "शांति", "hint": "Shaanti", "options": ["शांति", "युद्ध", "शोर", "गुस्सा"]},
        {"question": "What is 'Teacher' in Hindi?", "answer": "शिक्षक / गुरु", "hint": "Shikshak/Guru", "options": ["शिक्षक / गुरु", "विद्यार्थी", "डॉक्टर", "न्यायाधीश"]},
        {"question": "What is 'Justice' in Hindi?", "answer": "न्याय", "hint": "Nyaay", "options": ["न्याय", "अन्याय", "कानून", "सज़ा"]},
        {"question": "What is 'Freedom' in Hindi?", "answer": "आज़ादी", "hint": "Aazaadi", "options": ["आज़ादी", "गुलामी", "कैद", "बंधन"]},
        {"question": "What is 'Heart' in Hindi?", "answer": "दिल", "hint": "Dil", "options": ["दिल", "दिमाग", "आँख", "हाथ"]},
    ],

    # ==================================================
    # TAMIL  (~90 questions)
    # ==================================================
    "Tamil": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Tamil?", "answer": "வண்ணத்துப்பூச்சி", "hint": "Vannathu poochchi", "options": ["வண்ணத்துப்பூச்சி", "பறவை", "மீன்", "பூ"]},
        {"question": "What is 'Rainbow' in Tamil?", "answer": "வானவில்", "hint": "Vanavil", "options": ["வானவில்", "மேகம்", "மழை", "வெயில்"]},
        {"question": "What is 'Elephant' in Tamil?", "answer": "யானை", "hint": "Yaanai", "options": ["யானை", "சிங்கம்", "புலி", "கரடி"]},
        {"question": "What is 'Mountain' in Tamil?", "answer": "மலை", "hint": "Malai", "options": ["மலை", "ஆறு", "கடல்", "காடு"]},
        {"question": "What is 'Friendship' in Tamil?", "answer": "நட்பு", "hint": "Natpu", "options": ["நட்பு", "அன்பு", "கோபம்", "வெறுப்பு"]},
        {"question": "What is 'Doctor' in Tamil?", "answer": "மருத்துவர்", "hint": "Maruthuvar", "options": ["மருத்துவர்", "ஆசிரியர்", "காவலர்", "விவசாயி"]},
        {"question": "What is 'River' in Tamil?", "answer": "ஆறு", "hint": "Aaru", "options": ["ஆறு", "குளம்", "கடல்", "கிணறு"]},
        {"question": "What is 'Moon' in Tamil?", "answer": "நிலவு", "hint": "Nilavu", "options": ["நிலவு", "சூரியன்", "நட்சத்திரம்", "வானம்"]},
        {"question": "What is 'Wind' in Tamil?", "answer": "காற்று", "hint": "Kaatru", "options": ["காற்று", "நீர்", "நெருப்பு", "மண்"]},
        {"question": "What is 'Happiness' in Tamil?", "answer": "மகிழ்ச்சி", "hint": "Makilchchi", "options": ["மகிழ்ச்சி", "துக்கம்", "கோபம்", "பயம்"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Tamil?", "answer": "ஏழு", "hint": "Ezhu", "options": ["ஏழு", "ஆறு", "எட்டு", "ஒன்பது"]},
        {"question": "What is 'Eleven' in Tamil?", "answer": "பதினொன்று", "hint": "Pathinondru", "options": ["பதினொன்று", "பத்து", "பன்னிரண்டு", "பதினைந்து"]},
        {"question": "What is 'Hundred' in Tamil?", "answer": "நூறு", "hint": "Nooru", "options": ["நூறு", "ஆயிரம்", "ஐம்பது", "பத்து"]},
        {"question": "What is 'Thousand' in Tamil?", "answer": "ஆயிரம்", "hint": "Aayiram", "options": ["ஆயிரம்", "நூறு", "பத்து", "லட்சம்"]},
        {"question": "What is 'Twenty' in Tamil?", "answer": "இருபது", "hint": "Irupatu", "options": ["இருபது", "பத்து", "முப்பது", "நாற்பது"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Tamil?", "answer": "ஊதா", "hint": "Ootha", "options": ["ஊதா", "பச்சை", "நீலம்", "சிவப்பு"]},
        {"question": "What is 'Orange' in Tamil?", "answer": "ஆரஞ்சு நிறம்", "hint": "Aranchu niram", "options": ["ஆரஞ்சு நிறம்", "மஞ்சள்", "சிவப்பு", "இளஞ்சிவப்பு"]},
        {"question": "What is 'Brown' in Tamil?", "answer": "பழுப்பு", "hint": "Paluppu", "options": ["பழுப்பு", "வெள்ளை", "கருப்பு", "சாம்பல்"]},
        {"question": "What is 'Pink' in Tamil?", "answer": "இளஞ்சிவப்பு", "hint": "Ilanchivappu", "options": ["இளஞ்சிவப்பு", "பச்சை", "நீலம்", "பழுப்பு"]},
        {"question": "What is 'Golden' in Tamil?", "answer": "தங்க நிறம்", "hint": "Thanga niram", "options": ["தங்க நிறம்", "வெள்ளி நிறம்", "கருப்பு", "வெள்ளை"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Tamil?", "answer": "தோள்பட்டை", "hint": "Tholpattai", "options": ["தோள்பட்டை", "முழங்கை", "முழங்கால்", "குதிகால்"]},
        {"question": "What is 'Forehead' in Tamil?", "answer": "நெற்றி", "hint": "Netri", "options": ["நெற்றி", "கண்", "மூக்கு", "தலை"]},
        {"question": "What is 'Chin' in Tamil?", "answer": "கன்னம்", "hint": "Kannam", "options": ["கன்னம்", "கன்னத்தில்", "நெற்றி", "உதடு"]},
        {"question": "What is 'Thumb' in Tamil?", "answer": "கட்டைவிரல்", "hint": "Kattaiviral", "options": ["கட்டைவிரல்", "விரல்", "கை", "மணிக்கட்டு"]},
        {"question": "What is 'Knee' in Tamil?", "answer": "முழங்கால்", "hint": "Mulangaal", "options": ["முழங்கால்", "கால்", "தொடை", "கணுக்கால்"]},
        # --- Food ---
        {"question": "What is 'Rice' in Tamil?", "answer": "சோறு", "hint": "Soru", "options": ["சோறு", "ரொட்டி", "சாம்பார்", "இட்லி"]},
        {"question": "What is 'Milk' in Tamil?", "answer": "பால்", "hint": "Paal", "options": ["பால்", "நீர்", "ஜூஸ்", "தேநீர்"]},
        {"question": "What is 'Salt' in Tamil?", "answer": "உப்பு", "hint": "Uppu", "options": ["உப்பு", "சர்க்கரை", "மிளகாய்", "மஞ்சள்"]},
        {"question": "What is 'Mango' in Tamil?", "answer": "மாம்பழம்", "hint": "Maambalam", "options": ["மாம்பழம்", "வாழைப்பழம்", "திராட்சை", "ஆப்பிள்"]},
        {"question": "What is 'Banana' in Tamil?", "answer": "வாழைப்பழம்", "hint": "Vaalaipalam", "options": ["வாழைப்பழம்", "மாம்பழம்", "ஆப்பிள்", "திராட்சை"]},
        # --- Family ---
        {"question": "What is 'Elder sister' in Tamil?", "answer": "அக்கா", "hint": "Akka", "options": ["அக்கா", "அண்ணன்", "அம்மா", "அத்தை"]},
        {"question": "What is 'Grandfather' in Tamil?", "answer": "தாத்தா", "hint": "Thaathaa", "options": ["தாத்தா", "பாட்டி", "அப்பா", "மாமா"]},
        {"question": "What is 'Uncle' in Tamil?", "answer": "மாமா / சித்தப்பா", "hint": "Mama/Chittappa", "options": ["மாமா / சித்தப்பா", "அண்ணன்", "மகன்", "தம்பி"]},
        {"question": "What is 'Daughter' in Tamil?", "answer": "மகள்", "hint": "Magal", "options": ["மகள்", "மகன்", "அக்கா", "அம்மா"]},
        {"question": "What is 'Husband' in Tamil?", "answer": "கணவன்", "hint": "Kanavan", "options": ["கணவன்", "மனைவி", "அண்ணன்", "அப்பா"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Tamil?", "answer": "எனக்கு பசிக்கிறது", "hint": "Enakku pasikkithu", "options": ["எனக்கு பசிக்கிறது", "எனக்கு தூக்கம்", "எனக்கு தாகம்", "எனக்கு காய்ச்சல்"]},
        {"question": "What does 'நீங்கள் எப்படி இருக்கிறீர்கள்?' mean?", "answer": "How are you?", "hint": "A polite greeting question", "options": ["How are you?", "What is your name?", "Where are you going?", "What are you doing?"]},
        {"question": "What is 'Please' in Tamil?", "answer": "தயவுசெய்து", "hint": "Thayavu seidhu", "options": ["தயவுசெய்து", "நன்றி", "மன்னிக்கவும்", "வணக்கம்"]},
        {"question": "What is 'Sorry' in Tamil?", "answer": "மன்னிக்கவும்", "hint": "Mannikkavum", "options": ["மன்னிக்கவும்", "நன்றி", "தயவுசெய்து", "சரி"]},
        {"question": "What does 'வாருங்கள்' mean in Tamil?", "answer": "Please come", "hint": "An invitation", "options": ["Please come", "Please go", "Please sit", "Please wait"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Tamil?", "answer": "நாளை", "hint": "Naalai", "options": ["நாளை", "நேற்று", "இன்று", "மறுநாள்"]},
        {"question": "What is 'Monday' in Tamil?", "answer": "திங்கட்கிழமை", "hint": "Thingat kilamai", "options": ["திங்கட்கிழமை", "செவ்வாய்க்கிழமை", "சனிக்கிழமை", "ஞாயிற்றுக்கிழமை"]},
        {"question": "What is 'Morning' in Tamil?", "answer": "காலை", "hint": "Kaalai", "options": ["காலை", "மதியம்", "மாலை", "இரவு"]},
        {"question": "What is 'Year' in Tamil?", "answer": "ஆண்டு", "hint": "Aandu", "options": ["ஆண்டு", "மாதம்", "வாரம்", "நாள்"]},
        {"question": "What is 'Hour' in Tamil?", "answer": "மணி", "hint": "Mani", "options": ["மணி", "நிமிடம்", "விநாடி", "நாள்"]},
        # --- Places ---
        {"question": "What is 'Hospital' in Tamil?", "answer": "மருத்துவமனை", "hint": "Maruththuvamani", "options": ["மருத்துவமனை", "பள்ளி", "சந்தை", "கோயில்"]},
        {"question": "What is 'Temple' in Tamil?", "answer": "கோயில்", "hint": "Kovil", "options": ["கோயில்", "மசூதி", "தேவாலயம்", "மருத்துவமனை"]},
        {"question": "What is 'Library' in Tamil?", "answer": "நூலகம்", "hint": "Noolakam", "options": ["நூலகம்", "பள்ளி", "அலுவலகம்", "சந்தை"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Tamil?", "answer": "கிளி", "hint": "Kili", "options": ["கிளி", "காகம்", "குருவி", "மயில்"]},
        {"question": "What is 'Peacock' in Tamil?", "answer": "மயில்", "hint": "Mayil", "options": ["மயில்", "கிளி", "புறா", "கழுகு"]},
        {"question": "What is 'Cow' in Tamil?", "answer": "பசு", "hint": "Pasu", "options": ["பசு", "எருமை", "ஆடு", "செம்மறியாடு"]},
        {"question": "What is 'Tiger' in Tamil?", "answer": "புலி", "hint": "Puli", "options": ["புலி", "சிறுத்தை", "சிங்கம்", "கரடி"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Tamil?", "answer": "சாப்பிடு", "hint": "Saappidu", "options": ["சாப்பிடு", "குடி", "ஓடு", "நட"]},
        {"question": "What is 'To sleep' in Tamil?", "answer": "தூங்கு", "hint": "Thoong", "options": ["தூங்கு", "எழு", "உட்கார்", "நட"]},
        {"question": "What is 'To speak' in Tamil?", "answer": "பேசு", "hint": "Pesu", "options": ["பேசு", "கேள்", "படி", "எழுது"]},
        {"question": "What is 'To laugh' in Tamil?", "answer": "சிரி", "hint": "Chiri", "options": ["சிரி", "அழு", "பாடு", "ஆடு"]},
        {"question": "What is 'To run' in Tamil?", "answer": "ஓடு", "hint": "Odu", "options": ["ஓடு", "நட", "உட்கார்", "தூங்கு"]},
        # --- Adjectives ---
        {"question": "What is 'Beautiful' in Tamil?", "answer": "அழகான", "hint": "Alaga(a)na", "options": ["அழகான", "அசிங்கமான", "விந்தையான", "பயங்கரமான"]},
        {"question": "What is 'Brave' in Tamil?", "answer": "தைரியமான", "hint": "Thairiamana", "options": ["தைரியமான", "கோழையான", "சோம்பேறியான", "பேராசையான"]},
        {"question": "What is 'Fast' in Tamil?", "answer": "வேகமான", "hint": "Vegamana", "options": ["வேகமான", "மெதுவான", "நீண்ட", "குட்டையான"]},
        # --- Culture & Proverbs ---
        {"question": "Tamil is primarily spoken in which Indian state?", "answer": "Tamil Nadu", "hint": "Southern state", "options": ["Tamil Nadu", "Karnataka", "Kerala", "Andhra Pradesh"]},
        {"question": "What does 'ஆமாம்' mean in Tamil?", "answer": "Yes", "hint": "An affirmative word", "options": ["Yes", "No", "Maybe", "I don't know"]},
        {"question": "What does 'இல்லை' mean in Tamil?", "answer": "No", "hint": "A negative word", "options": ["No", "Yes", "Maybe", "Always"]},
        {"question": "What is 'Peace' in Tamil?", "answer": "அமைதி", "hint": "Amaithi", "options": ["அமைதி", "போர்", "கோலாகலம்", "கோபம்"]},
        {"question": "What is 'Victory' in Tamil?", "answer": "வெற்றி", "hint": "Vetri", "options": ["வெற்றி", "தோல்வி", "போராட்டம்", "முயற்சி"]},
        {"question": "What is 'Dream' in Tamil?", "answer": "கனவு", "hint": "Kanavu", "options": ["கனவு", "தூக்கம்", "ஆசை", "நினைவு"]},
        {"question": "What is 'Knowledge' in Tamil?", "answer": "அறிவு", "hint": "Arivu", "options": ["அறிவு", "அறியாமை", "கல்வி", "புத்தி"]},
        {"question": "What is 'Language' in Tamil?", "answer": "மொழி", "hint": "Moli", "options": ["மொழி", "வார்த்தை", "எழுத்து", "பேச்சு"]},
        {"question": "What is 'Teacher' in Tamil?", "answer": "ஆசிரியர்", "hint": "Aasiriyar", "options": ["ஆசிரியர்", "மாணவர்", "மருத்துவர்", "நீதிபதி"]},
        {"question": "What is 'Freedom' in Tamil?", "answer": "சுதந்திரம்", "hint": "Suthanthiram", "options": ["சுதந்திரம்", "அடிமைத்தனம்", "சிறை", "கட்டுப்பாடு"]},
    ],

    # ==================================================
    # TELUGU  (~90 questions)
    # ==================================================
    "Telugu": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Telugu?", "answer": "సీతాకోకచిలుక", "hint": "Seetaakoka chiluka", "options": ["సీతాకోకచిలుక", "పక్షి", "చేప", "పువ్వు"]},
        {"question": "What is 'Rainbow' in Telugu?", "answer": "ఇంద్రధనుస్సు", "hint": "Indradhanussu", "options": ["ఇంద్రధనుస్సు", "మేఘం", "వర్షం", "ఎండ"]},
        {"question": "What is 'Elephant' in Telugu?", "answer": "ఏనుగు", "hint": "Ènugu", "options": ["ఏనుగు", "సింహం", "పులి", "ఎలుగుబంటి"]},
        {"question": "What is 'Mountain' in Telugu?", "answer": "పర్వతం", "hint": "Parvatam", "options": ["పర్వతం", "నది", "సముద్రం", "అడవి"]},
        {"question": "What is 'Friendship' in Telugu?", "answer": "స్నేహం", "hint": "Sneham", "options": ["స్నేహం", "ప్రేమ", "కోపం", "ద్వేషం"]},
        {"question": "What is 'Doctor' in Telugu?", "answer": "వైద్యుడు", "hint": "Vaidyudu", "options": ["వైద్యుడు", "ఉపాధ్యాయుడు", "పోలీసు", "రైతు"]},
        {"question": "What is 'River' in Telugu?", "answer": "నది", "hint": "Nadi", "options": ["నది", "చెరువు", "సముద్రం", "బావి"]},
        {"question": "What is 'Moon' in Telugu?", "answer": "చంద్రుడు", "hint": "Chandrudu", "options": ["చంద్రుడు", "సూర్యుడు", "నక్షత్రం", "ఆకాశం"]},
        {"question": "What is 'Wind' in Telugu?", "answer": "గాలి", "hint": "Gaali", "options": ["గాలి", "నీరు", "నిప్పు", "మట్టి"]},
        {"question": "What is 'Happiness' in Telugu?", "answer": "ఆనందం", "hint": "Aanandham", "options": ["ఆనందం", "దుఃఖం", "కోపం", "భయం"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Telugu?", "answer": "ఏడు", "hint": "Edu", "options": ["ఏడు", "ఆరు", "ఎనిమిది", "తొమ్మిది"]},
        {"question": "What is 'Eleven' in Telugu?", "answer": "పదకొండు", "hint": "Padakondu", "options": ["పదకొండు", "పది", "పన్నెండు", "పదిహేను"]},
        {"question": "What is 'Hundred' in Telugu?", "answer": "వంద", "hint": "Vanda", "options": ["వంద", "వేయి", "ఏభై", "పది"]},
        {"question": "What is 'Twenty' in Telugu?", "answer": "ఇరవై", "hint": "Iravai", "options": ["ఇరవై", "పది", "ముప్పై", "నలభై"]},
        {"question": "What is 'Fifty' in Telugu?", "answer": "యాభై", "hint": "Yaabhai", "options": ["యాభై", "నలభై", "అరవై", "డెబ్భై"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Telugu?", "answer": "ఊదా రంగు", "hint": "Ooda rangu", "options": ["ఊదా రంగు", "పచ్చ", "నీలం", "ఎరుపు"]},
        {"question": "What is 'Orange' in Telugu?", "answer": "నారింజ రంగు", "hint": "Naarinja rangu", "options": ["నారింజ రంగు", "పసుపు", "ఎరుపు", "గులాబీ"]},
        {"question": "What is 'Brown' in Telugu?", "answer": "గోధుమ రంగు", "hint": "Godhuma rangu", "options": ["గోధుమ రంగు", "తెలుపు", "నలుపు", "బూడిద"]},
        {"question": "What is 'Pink' in Telugu?", "answer": "గులాబీ రంగు", "hint": "Gulaabi rangu", "options": ["గులాబీ రంగు", "పచ్చ", "నీలం", "గోధుమ"]},
        {"question": "What is 'Golden' in Telugu?", "answer": "బంగారు రంగు", "hint": "Bangaaru rangu", "options": ["బంగారు రంగు", "వెండి రంగు", "నలుపు", "తెలుపు"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Telugu?", "answer": "భుజం", "hint": "Bhujam", "options": ["భుజం", "మోచేయి", "మోకాలు", "మడమ"]},
        {"question": "What is 'Forehead' in Telugu?", "answer": "నుదురు", "hint": "Nuduru", "options": ["నుదురు", "కన్ను", "ముక్కు", "తల"]},
        {"question": "What is 'Knee' in Telugu?", "answer": "మోకాలు", "hint": "Mokalu", "options": ["మోకాలు", "కాలు", "తొడ", "చీలమండ"]},
        {"question": "What is 'Thumb' in Telugu?", "answer": "బొటనవేలు", "hint": "Botanavelu", "options": ["బొటనవేలు", "వేలు", "చేయి", "మణికట్టు"]},
        # --- Food ---
        {"question": "What is 'Rice' in Telugu?", "answer": "అన్నం", "hint": "Annam", "options": ["అన్నం", "రొట్టె", "పప్పు", "కూర"]},
        {"question": "What is 'Milk' in Telugu?", "answer": "పాలు", "hint": "Paalu", "options": ["పాలు", "నీరు", "జ్యూస్", "టీ"]},
        {"question": "What is 'Salt' in Telugu?", "answer": "ఉప్పు", "hint": "Uppu", "options": ["ఉప్పు", "చక్కెర", "మిర్చి", "పసుపు"]},
        {"question": "What is 'Mango' in Telugu?", "answer": "మామిడి పండు", "hint": "Maamidi pandu", "options": ["మామిడి పండు", "అరటి పండు", "ద్రాక్ష", "ఆపిల్"]},
        {"question": "What is 'Onion' in Telugu?", "answer": "ఉల్లిపాయ", "hint": "Ullipaya", "options": ["ఉల్లిపాయ", "టొమాటో", "బంగాళాదుంప", "క్యారెట్"]},
        # --- Family ---
        {"question": "What is 'Sister' in Telugu?", "answer": "అక్క / చెల్లి", "hint": "Akka/Chelli", "options": ["అక్క / చెల్లి", "అన్న", "అమ్మ", "అత్త"]},
        {"question": "What is 'Grandfather' in Telugu?", "answer": "తాత", "hint": "Thaata", "options": ["తాత", "నానమ్మ", "నాన్న", "మావయ్య"]},
        {"question": "What is 'Daughter' in Telugu?", "answer": "కూతురు", "hint": "Kooturu", "options": ["కూతురు", "కొడుకు", "అక్క", "అమ్మ"]},
        {"question": "What is 'Husband' in Telugu?", "answer": "భర్త", "hint": "Bhartha", "options": ["భర్త", "భార్య", "అన్న", "నాన్న"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Telugu?", "answer": "నాకు ఆకలిగా ఉంది", "hint": "Naaku akaliga undi", "options": ["నాకు ఆకలిగా ఉంది", "నాకు నిద్రగా ఉంది", "నాకు దాహంగా ఉంది", "నాకు జ్వరంగా ఉంది"]},
        {"question": "What does 'మీరు ఎలా ఉన్నారు?' mean?", "answer": "How are you?", "hint": "A polite enquiry", "options": ["How are you?", "What is your name?", "Where do you live?", "What do you do?"]},
        {"question": "What is 'Please' in Telugu?", "answer": "దయచేసి", "hint": "Dayachesi", "options": ["దయచేసి", "ధన్యవాదాలు", "క్షమించండి", "నమస్కారం"]},
        {"question": "What is 'Sorry' in Telugu?", "answer": "క్షమించండి", "hint": "Kshaminchandhi", "options": ["క్షమించండి", "ధన్యవాదాలు", "దయచేసి", "సరే"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Telugu?", "answer": "రేపు", "hint": "Reppu", "options": ["రేపు", "నిన్న", "ఈరోజు", "మొన్న"]},
        {"question": "What is 'Monday' in Telugu?", "answer": "సోమవారం", "hint": "Somawaaram", "options": ["సోమవారం", "మంగళవారం", "శనివారం", "ఆదివారం"]},
        {"question": "What is 'Morning' in Telugu?", "answer": "ఉదయం", "hint": "Udayam", "options": ["ఉదయం", "మధ్యాహ్నం", "సాయంత్రం", "రాత్రి"]},
        {"question": "What is 'Year' in Telugu?", "answer": "సంవత్సరం", "hint": "Samvatsaram", "options": ["సంవత్సరం", "నెల", "వారం", "రోజు"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Telugu?", "answer": "చిలుక", "hint": "Chiluka", "options": ["చిలుక", "కాకి", "గోరువంక", "నెమలి"]},
        {"question": "What is 'Peacock' in Telugu?", "answer": "నెమలి", "hint": "Nemali", "options": ["నెమలి", "చిలుక", "పావురం", "డేగ"]},
        {"question": "What is 'Cow' in Telugu?", "answer": "ఆవు", "hint": "Aavu", "options": ["ఆవు", "గేదె", "మేక", "గొర్రె"]},
        {"question": "What is 'Tiger' in Telugu?", "answer": "పులి", "hint": "Puli", "options": ["పులి", "చిరుత", "సింహం", "ఎలుగుబంటి"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Telugu?", "answer": "తినడం", "hint": "Tinadam", "options": ["తినడం", "తాగడం", "పరిగెత్తడం", "నడవడం"]},
        {"question": "What is 'To sleep' in Telugu?", "answer": "నిద్రపోవడం", "hint": "Nidrapovadham", "options": ["నిద్రపోవడం", "లేవడం", "కూర్చోవడం", "నడవడం"]},
        {"question": "What is 'To speak' in Telugu?", "answer": "మాట్లాడటం", "hint": "Maatlaadadam", "options": ["మాట్లాడటం", "వినడం", "చదవడం", "రాయడం"]},
        {"question": "What is 'To laugh' in Telugu?", "answer": "నవ్వడం", "hint": "Navvadam", "options": ["నవ్వడం", "ఏడవడం", "పాడటం", "ఆడడం"]},
        # --- Adjectives & More ---
        {"question": "What is 'Beautiful' in Telugu?", "answer": "అందమైన", "hint": "Andhamaina", "options": ["అందమైన", "అగోచర", "విచిత్రమైన", "భయంకరమైన"]},
        {"question": "What is 'Brave' in Telugu?", "answer": "ధైర్యవంతుడు", "hint": "Dhairyavanthudu", "options": ["ధైర్యవంతుడు", "పిరికివాడు", "సోమరి", "అత్యాశగలవాడు"]},
        {"question": "What is 'Fast' in Telugu?", "answer": "వేగంగా", "hint": "Veganga", "options": ["వేగంగా", "నెమ్మదిగా", "పొడవుగా", "పొట్టిగా"]},
        {"question": "What is 'Rain' in Telugu?", "answer": "వర్షం", "hint": "Varsham", "options": ["వర్షం", "ఎండ", "గాలి", "మంచు"]},
        {"question": "What is 'Sky' in Telugu?", "answer": "ఆకాశం", "hint": "Aakaasam", "options": ["ఆకాశం", "భూమి", "నీరు", "అడవి"]},
        {"question": "What is 'Dream' in Telugu?", "answer": "కల", "hint": "Kala", "options": ["కల", "నిద్ర", "కోరిక", "జ్ఞాపకం"]},
        {"question": "What is 'Knowledge' in Telugu?", "answer": "జ్ఞానం", "hint": "Jnaanam", "options": ["జ్ఞానం", "అజ్ఞానం", "విద్య", "బుద్ధి"]},
        {"question": "What is 'Peace' in Telugu?", "answer": "శాంతి", "hint": "Shaanthi", "options": ["శాంతి", "యుద్ధం", "కోలాహలం", "కోపం"]},
        {"question": "What is 'Victory' in Telugu?", "answer": "విజయం", "hint": "Vijayam", "options": ["విజయం", "ఓటమి", "పోరాటం", "ప్రయత్నం"]},
        {"question": "What is 'Teacher' in Telugu?", "answer": "ఉపాధ్యాయుడు", "hint": "Upadhyayudu", "options": ["ఉపాధ్యాయుడు", "విద్యార్థి", "వైద్యుడు", "న్యాయమూర్తి"]},
        {"question": "What is 'Freedom' in Telugu?", "answer": "స్వాతంత్ర్యం", "hint": "Svaatantryam", "options": ["స్వాతంత్ర్యం", "బానిసత్వం", "కారాగారం", "బంధం"]},
        {"question": "Telugu is primarily spoken in which Indian state?", "answer": "Andhra Pradesh / Telangana", "hint": "Two states share this language", "options": ["Andhra Pradesh / Telangana", "Karnataka", "Tamil Nadu", "Kerala"]},
        {"question": "What does 'అవును' mean in Telugu?", "answer": "Yes", "hint": "An affirmative response", "options": ["Yes", "No", "Maybe", "Never"]},
        {"question": "What does 'కాదు' mean in Telugu?", "answer": "No / It is not", "hint": "A negative response", "options": ["No / It is not", "Yes", "Maybe", "Always"]},
        {"question": "What is 'Language' in Telugu?", "answer": "భాష", "hint": "Bhaasha", "options": ["భాష", "మాట", "అక్షరం", "పదం"]},
        {"question": "What is 'Village' in Telugu?", "answer": "గ్రామం", "hint": "Graamam", "options": ["గ్రామం", "నగరం", "జిల్లా", "రాష్ట్రం"]},
        {"question": "What is 'Gold' in Telugu?", "answer": "బంగారం", "hint": "Bangaaram", "options": ["బంగారం", "వెండి", "ఇనుము", "రాగి"]},
    ],

    # ==================================================
    # MALAYALAM  (~90 questions)
    # ==================================================
    "Malayalam": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Malayalam?", "answer": "ചിത്രശലഭം", "hint": "Chitrashalabham", "options": ["ചിത്രശലഭം", "പക്ഷി", "മത്സ്യം", "പൂവ്"]},
        {"question": "What is 'Rainbow' in Malayalam?", "answer": "മഴവില്ല്", "hint": "Malavillu", "options": ["മഴവില്ല്", "മേഘം", "മഴ", "വെയില്‍"]},
        {"question": "What is 'Elephant' in Malayalam?", "answer": "ആന", "hint": "Aana", "options": ["ആന", "സിംഹം", "കടുവ", "കരടി"]},
        {"question": "What is 'Mountain' in Malayalam?", "answer": "മല", "hint": "Mala", "options": ["മല", "നദി", "കടൽ", "കാട്"]},
        {"question": "What is 'Friendship' in Malayalam?", "answer": "സൗഹൃദം", "hint": "Sauhrdam", "options": ["സൗഹൃദം", "സ്നേഹം", "കോപം", "വെറുപ്പ്"]},
        {"question": "What is 'Doctor' in Malayalam?", "answer": "ഡോക്ടർ / വൈദ്യൻ", "hint": "Doctor/Vaidyan", "options": ["ഡോക്ടർ / വൈദ്യൻ", "അദ്ധ്യാപകൻ", "പോലീസ്", "കർഷകൻ"]},
        {"question": "What is 'River' in Malayalam?", "answer": "നദി", "hint": "Nadi", "options": ["നദി", "കുളം", "കടൽ", "കിണർ"]},
        {"question": "What is 'Moon' in Malayalam?", "answer": "ചന്ദ്രൻ", "hint": "Chandran", "options": ["ചന്ദ്രൻ", "സൂര്യൻ", "നക്ഷത്രം", "ആകാശം"]},
        {"question": "What is 'Wind' in Malayalam?", "answer": "കാറ്റ്", "hint": "Kaattu", "options": ["കാറ്റ്", "വെള്ളം", "തീ", "മണ്ണ്"]},
        {"question": "What is 'Happiness' in Malayalam?", "answer": "സന്തോഷം", "hint": "Santhosham", "options": ["സന്തോഷം", "ദുഃഖം", "കോപം", "ഭയം"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Malayalam?", "answer": "ഏഴ്", "hint": "Ezh", "options": ["ഏഴ്", "ആറ്", "എട്ട്", "ഒൻപത്"]},
        {"question": "What is 'Eleven' in Malayalam?", "answer": "പതിനൊന്ന്", "hint": "Pathinonnu", "options": ["പതിനൊന്ന്", "പത്ത്", "പന്ത്രണ്ട്", "പതിനഞ്ച്"]},
        {"question": "What is 'Hundred' in Malayalam?", "answer": "നൂറ്", "hint": "Nooru", "options": ["നൂറ്", "ആയിരം", "അമ്പത്", "പത്ത്"]},
        {"question": "What is 'Twenty' in Malayalam?", "answer": "ഇരുപത്", "hint": "Irupat", "options": ["ഇരുപത്", "പത്ത്", "മുപ്പത്", "നാൽപ്പത്"]},
        {"question": "What is 'Fifty' in Malayalam?", "answer": "അമ്പത്", "hint": "Ampat", "options": ["അമ്പത്", "നാൽപ്പത്", "അറുപത്", "എഴുപത്"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Malayalam?", "answer": "ഊതനിറം", "hint": "Oota niram", "options": ["ഊതനിറം", "പച്ച", "നീല", "ചുവപ്പ്"]},
        {"question": "What is 'Orange' in Malayalam?", "answer": "ഓറഞ്ച് നിറം", "hint": "Orange niram", "options": ["ഓറഞ്ച് നിറം", "മഞ്ഞ", "ചുവപ്പ്", "ഗുലാബി"]},
        {"question": "What is 'Brown' in Malayalam?", "answer": "തവിട്ടുനിറം", "hint": "Thavittu niram", "options": ["തവിട്ടുനിറം", "വെള്ള", "കറുപ്പ്", "ചാരനിറം"]},
        {"question": "What is 'Pink' in Malayalam?", "answer": "ഇളം ചുവപ്പ്", "hint": "Ilam chuvappu", "options": ["ഇളം ചുവപ്പ്", "പച്ച", "നീല", "തവിട്ട്"]},
        {"question": "What is 'Golden' in Malayalam?", "answer": "സ്വർണ്ണ നിറം", "hint": "Svarna niram", "options": ["സ്വർണ്ണ നിറം", "വെള്ളി നിറം", "കറുപ്പ്", "വെള്ള"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Malayalam?", "answer": "ചുമൽ", "hint": "Chumal", "options": ["ചുമൽ", "മുട്ട്", "കണ്ണ്", "കൈ"]},
        {"question": "What is 'Forehead' in Malayalam?", "answer": "നെറ്റി", "hint": "Netti", "options": ["നെറ്റി", "കണ്ണ്", "മൂക്ക്", "തല"]},
        {"question": "What is 'Knee' in Malayalam?", "answer": "മുട്ട്", "hint": "Muttu", "options": ["മുട്ട്", "കാൽ", "തുട", "കണങ്കാൽ"]},
        {"question": "What is 'Thumb' in Malayalam?", "answer": "തള്ളവിരൽ", "hint": "Thalla viral", "options": ["തള്ളവിരൽ", "വിരൽ", "കൈ", "കൈത്തണ്ട"]},
        # --- Food ---
        {"question": "What is 'Rice' in Malayalam?", "answer": "ചോറ്", "hint": "Choru", "options": ["ചോറ്", "റൊട്ടി", "സാമ്പാർ", "ഇഡ്ഡലി"]},
        {"question": "What is 'Milk' in Malayalam?", "answer": "പാൽ", "hint": "Paal", "options": ["പാൽ", "വെള്ളം", "ജ്യൂസ്", "ചായ"]},
        {"question": "What is 'Salt' in Malayalam?", "answer": "ഉപ്പ്", "hint": "Uppu", "options": ["ഉപ്പ്", "പഞ്ചസാര", "മുളക്", "മഞ്ഞൾ"]},
        {"question": "What is 'Mango' in Malayalam?", "answer": "മാങ്ങ", "hint": "Maanga", "options": ["മാങ്ങ", "വാഴപ്പഴം", "മുന്തിരി", "ആപ്പിൾ"]},
        {"question": "What is 'Banana' in Malayalam?", "answer": "വാഴപ്പഴം", "hint": "Vaalapazham", "options": ["വാഴപ്പഴം", "മാങ്ങ", "ആപ്പിൾ", "മുന്തിരി"]},
        # --- Family ---
        {"question": "What is 'Elder sister' in Malayalam?", "answer": "ചേച്ചി", "hint": "Chechi", "options": ["ചേച്ചി", "ചേട്ടൻ", "അമ്മ", "അത്ത"]},
        {"question": "What is 'Grandfather' in Malayalam?", "answer": "മുത്തശ്ശൻ", "hint": "Muthasshan", "options": ["മുത്തശ്ശൻ", "മുത്തശ്ശി", "അച്ഛൻ", "മാമൻ"]},
        {"question": "What is 'Daughter' in Malayalam?", "answer": "മകൾ", "hint": "Makal", "options": ["മകൾ", "മകൻ", "ചേച്ചി", "അമ്മ"]},
        {"question": "What is 'Husband' in Malayalam?", "answer": "ഭർത്താവ്", "hint": "Bhartthaavu", "options": ["ഭർത്താവ്", "ഭാര്യ", "ചേട്ടൻ", "അച്ഛൻ"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Malayalam?", "answer": "എനിക്ക് വിശക്കുന്നു", "hint": "Enikku vishakkunnu", "options": ["എനിക്ക് വിശക്കുന്നു", "എനിക്ക് ഉറക്കം", "എനിക്ക് ദാഹം", "എനിക്ക് പനി"]},
        {"question": "What does 'നിങ്ങൾ എങ്ങനെ ഉണ്ട്?' mean?", "answer": "How are you?", "hint": "A polite greeting", "options": ["How are you?", "What is your name?", "Where are you going?", "What do you do?"]},
        {"question": "What is 'Please' in Malayalam?", "answer": "ദയവായി", "hint": "Dayavayi", "options": ["ദയവായി", "നന്ദി", "ക്ഷമിക്കണം", "നമസ്കാരം"]},
        {"question": "What is 'Sorry' in Malayalam?", "answer": "ക്ഷമിക്കണം", "hint": "KshamikkaNam", "options": ["ക്ഷമിക്കണം", "നന്ദി", "ദയവായി", "ശരി"]},
        {"question": "What does 'വരൂ' mean in Malayalam?", "answer": "Please come", "hint": "An invitation", "options": ["Please come", "Please go", "Please sit", "Please wait"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Malayalam?", "answer": "നാളെ", "hint": "Naale", "options": ["നാളെ", "ഇന്നലെ", "ഇന്ന്", "മറ്റന്നാൾ"]},
        {"question": "What is 'Monday' in Malayalam?", "answer": "തിങ്കളാഴ്ച", "hint": "Thingalaazcha", "options": ["തിങ്കളാഴ്ച", "ചൊവ്വാഴ്ച", "ശനിയാഴ്ച", "ഞായറാഴ്ച"]},
        {"question": "What is 'Morning' in Malayalam?", "answer": "രാവിലെ", "hint": "Raavile", "options": ["രാവിലെ", "ഉച്ചക്ക്", "വൈകിട്ട്", "രാത്രി"]},
        {"question": "What is 'Year' in Malayalam?", "answer": "വർഷം", "hint": "Varsham", "options": ["വർഷം", "മാസം", "ആഴ്ച", "ദിവസം"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Malayalam?", "answer": "തത്ത", "hint": "Thatha", "options": ["തത്ത", "കാക്ക", "കുരുവി", "മയിൽ"]},
        {"question": "What is 'Peacock' in Malayalam?", "answer": "മയിൽ", "hint": "Mayil", "options": ["മയിൽ", "തത്ത", "പ്രാവ്", "കഴുകൻ"]},
        {"question": "What is 'Cow' in Malayalam?", "answer": "പശു", "hint": "Pashu", "options": ["പശു", "പോത്ത്", "ആട്", "ചെമ്മരിയാട്"]},
        {"question": "What is 'Tiger' in Malayalam?", "answer": "കടുവ", "hint": "Kaduva", "options": ["കടുവ", "ചീറ്റ", "സിംഹം", "കരടി"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Malayalam?", "answer": "കഴിക്കുക", "hint": "Kazhikkuka", "options": ["കഴിക്കുക", "കുടിക്കുക", "ഓടുക", "നടക്കുക"]},
        {"question": "What is 'To sleep' in Malayalam?", "answer": "ഉറങ്ങുക", "hint": "Uranguka", "options": ["ഉറങ്ങുക", "എഴുന്നേൽക്കുക", "ഇരിക്കുക", "നടക്കുക"]},
        {"question": "What is 'To speak' in Malayalam?", "answer": "സംസാരിക്കുക", "hint": "Samsaarikkuka", "options": ["സംസാരിക്കുക", "കേൾക്കുക", "വായിക്കുക", "എഴുതുക"]},
        {"question": "What is 'To laugh' in Malayalam?", "answer": "ചിരിക്കുക", "hint": "Chirikkuka", "options": ["ചിരിക്കുക", "കരയുക", "പാടുക", "ആടുക"]},
        # --- Adjectives & More ---
        {"question": "What is 'Beautiful' in Malayalam?", "answer": "സുന്ദരം", "hint": "Sundharam", "options": ["സുന്ദരം", "വൃത്തികേട്", "വിചിത്രം", "ഭയങ്കരം"]},
        {"question": "What is 'Brave' in Malayalam?", "answer": "ധൈര്യശാലി", "hint": "Dhairyashaali", "options": ["ധൈര്യശാലി", "ഭീരു", "മടിയൻ", "ആർത്തി"]},
        {"question": "What is 'Fast' in Malayalam?", "answer": "വേഗം", "hint": "Vegam", "options": ["വേഗം", "പതുക്കെ", "നീളമുള്ള", "കുറിയ"]},
        {"question": "What is 'Rain' in Malayalam?", "answer": "മഴ", "hint": "Mala", "options": ["മഴ", "വെയില്‍", "കാറ്റ്", "മഞ്ഞ്"]},
        {"question": "What is 'Sky' in Malayalam?", "answer": "ആകാശം", "hint": "Aakaasham", "options": ["ആകാശം", "ഭൂമി", "വെള്ളം", "കാട്"]},
        {"question": "What is 'Dream' in Malayalam?", "answer": "സ്വപ്നം", "hint": "Svapnam", "options": ["സ്വപ്നം", "ഉറക്കം", "ആഗ്രഹം", "ഓർമ്മ"]},
        {"question": "What is 'Knowledge' in Malayalam?", "answer": "അറിവ്", "hint": "Arivu", "options": ["അറിവ്", "അജ്ഞത", "വിദ്യ", "ബുദ്ധി"]},
        {"question": "What is 'Peace' in Malayalam?", "answer": "സമാധാനം", "hint": "Samaadhaanam", "options": ["സമാധാനം", "യുദ്ധം", "ബഹളം", "കോപം"]},
        {"question": "What is 'Victory' in Malayalam?", "answer": "വിജയം", "hint": "Vijayam", "options": ["വിജയം", "പരാജയം", "പോരാട്ടം", "ശ്രമം"]},
        {"question": "What is 'Teacher' in Malayalam?", "answer": "അദ്ധ്യാപകൻ", "hint": "Adhyaapakan", "options": ["അദ്ധ്യാപകൻ", "വിദ്യാർത്ഥി", "ഡോക്ടർ", "ജഡ്ജി"]},
        {"question": "Malayalam is primarily spoken in which Indian state?", "answer": "Kerala", "hint": "God's own country", "options": ["Kerala", "Karnataka", "Tamil Nadu", "Goa"]},
        {"question": "What does 'ആണ്' mean in Malayalam?", "answer": "Yes / It is", "hint": "An affirmative word", "options": ["Yes / It is", "No", "Maybe", "Never"]},
        {"question": "What is 'Language' in Malayalam?", "answer": "ഭാഷ", "hint": "Bhasha", "options": ["ഭാഷ", "വാക്ക്", "അക്ഷരം", "പദം"]},
        {"question": "What is 'Village' in Malayalam?", "answer": "ഗ്രാമം", "hint": "Graamam", "options": ["ഗ്രാമം", "നഗരം", "ജില്ല", "സംസ്ഥാനം"]},
        {"question": "What is 'Gold' in Malayalam?", "answer": "സ്വർണ്ണം", "hint": "Svarnam", "options": ["സ്വർണ്ണം", "വെള്ളി", "ഇരുമ്പ്", "ചെമ്പ്"]},
        {"question": "What is 'Freedom' in Malayalam?", "answer": "സ്വാതന്ത്ര്യം", "hint": "Svaathantryam", "options": ["സ്വാതന്ത്ര്യം", "അടിമത്തം", "തടവ്", "ബന്ധനം"]},
        {"question": "What is 'Heart' in Malayalam?", "answer": "ഹൃദയം", "hint": "Hridayam", "options": ["ഹൃദയം", "തലച്ചോറ്", "കണ്ണ്", "കൈ"]},
    ],

    # ==================================================
    # MARATHI  (~90 questions)
    # ==================================================
    "Marathi": [
        # --- Basic Vocabulary ---
        {"question": "What is 'Butterfly' in Marathi?", "answer": "फुलपाखरू", "hint": "Phulpaakharu", "options": ["फुलपाखरू", "पक्षी", "मासा", "फूल"]},
        {"question": "What is 'Rainbow' in Marathi?", "answer": "इंद्रधनुष्य", "hint": "Indradhanushya", "options": ["इंद्रधनुष्य", "ढग", "पाऊस", "ऊन"]},
        {"question": "What is 'Elephant' in Marathi?", "answer": "हत्ती", "hint": "Hatti", "options": ["हत्ती", "सिंह", "वाघ", "अस्वल"]},
        {"question": "What is 'Mountain' in Marathi?", "answer": "पर्वत", "hint": "Parvat", "options": ["पर्वत", "नदी", "समुद्र", "जंगल"]},
        {"question": "What is 'Friendship' in Marathi?", "answer": "मैत्री", "hint": "Maitri", "options": ["मैत्री", "प्रेम", "राग", "द्वेष"]},
        {"question": "What is 'Doctor' in Marathi?", "answer": "डॉक्टर / वैद्य", "hint": "Doctor/Vaidya", "options": ["डॉक्टर / वैद्य", "शिक्षक", "पोलीस", "शेतकरी"]},
        {"question": "What is 'River' in Marathi?", "answer": "नदी", "hint": "Nadi", "options": ["नदी", "तलाव", "समुद्र", "विहीर"]},
        {"question": "What is 'Moon' in Marathi?", "answer": "चंद्र", "hint": "Chandra", "options": ["चंद्र", "सूर्य", "तारा", "आकाश"]},
        {"question": "What is 'Wind' in Marathi?", "answer": "वारा", "hint": "Vaara", "options": ["वारा", "पाणी", "आग", "माती"]},
        {"question": "What is 'Happiness' in Marathi?", "answer": "आनंद", "hint": "Aanand", "options": ["आनंद", "दुःख", "राग", "भीती"]},
        # --- Numbers ---
        {"question": "What is 'Seven' in Marathi?", "answer": "सात", "hint": "Saat", "options": ["सात", "सहा", "आठ", "नऊ"]},
        {"question": "What is 'Eleven' in Marathi?", "answer": "अकरा", "hint": "Akara", "options": ["अकरा", "दहा", "बारा", "पंधरा"]},
        {"question": "What is 'Hundred' in Marathi?", "answer": "शंभर", "hint": "Shambhar", "options": ["शंभर", "हजार", "पन्नास", "दहा"]},
        {"question": "What is 'Twenty' in Marathi?", "answer": "वीस", "hint": "Vees", "options": ["वीस", "दहा", "तीस", "चाळीस"]},
        {"question": "What is 'Fifty' in Marathi?", "answer": "पन्नास", "hint": "Pannaas", "options": ["पन्नास", "चाळीस", "साठ", "सत्तर"]},
        # --- Colors ---
        {"question": "What is 'Purple' in Marathi?", "answer": "जांभळा", "hint": "Jaambhala", "options": ["जांभळा", "हिरवा", "निळा", "लाल"]},
        {"question": "What is 'Orange' in Marathi?", "answer": "नारिंगी", "hint": "Naaringi", "options": ["नारिंगी", "पिवळा", "लाल", "गुलाबी"]},
        {"question": "What is 'Brown' in Marathi?", "answer": "तपकिरी", "hint": "Tapkiri", "options": ["तपकिरी", "पांढरा", "काळा", "राखाडी"]},
        {"question": "What is 'Pink' in Marathi?", "answer": "गुलाबी", "hint": "Gulaabi", "options": ["गुलाबी", "हिरवा", "निळा", "तपकिरी"]},
        {"question": "What is 'Golden' in Marathi?", "answer": "सोनेरी", "hint": "Soneri", "options": ["सोनेरी", "चांदेरी", "काळा", "पांढरा"]},
        # --- Body Parts ---
        {"question": "What is 'Shoulder' in Marathi?", "answer": "खांदा", "hint": "Khaanda", "options": ["खांदा", "कोपर", "गुडघा", "टाच"]},
        {"question": "What is 'Forehead' in Marathi?", "answer": "कपाळ", "hint": "Kapaal", "options": ["कपाळ", "डोळा", "नाक", "डोके"]},
        {"question": "What is 'Chin' in Marathi?", "answer": "हनुवटी", "hint": "Hanuvati", "options": ["हनुवटी", "गाल", "कपाळ", "ओठ"]},
        {"question": "What is 'Thumb' in Marathi?", "answer": "अंगठा", "hint": "Angtha", "options": ["अंगठा", "बोट", "हात", "मनगट"]},
        {"question": "What is 'Knee' in Marathi?", "answer": "गुडघा", "hint": "Gudgha", "options": ["गुडघा", "पाय", "मांडी", "घोटा"]},
        # --- Food ---
        {"question": "What is 'Rice' in Marathi?", "answer": "भात", "hint": "Bhaat", "options": ["भात", "पोळी", "आमटी", "उपमा"]},
        {"question": "What is 'Milk' in Marathi?", "answer": "दूध", "hint": "Doodh", "options": ["दूध", "पाणी", "ज्यूस", "चहा"]},
        {"question": "What is 'Salt' in Marathi?", "answer": "मीठ", "hint": "Meeth", "options": ["मीठ", "साखर", "मिरची", "हळद"]},
        {"question": "What is 'Mango' in Marathi?", "answer": "आंबा", "hint": "Aamba", "options": ["आंबा", "केळ", "द्राक्ष", "सफरचंद"]},
        {"question": "What is 'Onion' in Marathi?", "answer": "कांदा", "hint": "Kaanda", "options": ["कांदा", "टोमॅटो", "बटाटा", "गाजर"]},
        # --- Family ---
        {"question": "What is 'Sister' in Marathi?", "answer": "बहीण", "hint": "Baheen", "options": ["बहीण", "भाऊ", "आई", "काकू"]},
        {"question": "What is 'Grandfather' in Marathi?", "answer": "आजोबा", "hint": "Aajoba", "options": ["आजोबा", "आजी", "बाबा", "काका"]},
        {"question": "What is 'Uncle' in Marathi?", "answer": "काका / मामा", "hint": "Kaaka/Maama", "options": ["काका / मामा", "भाऊ", "मुलगा", "दादा"]},
        {"question": "What is 'Daughter' in Marathi?", "answer": "मुलगी", "hint": "Mulgi", "options": ["मुलगी", "मुलगा", "बहीण", "आई"]},
        {"question": "What is 'Husband' in Marathi?", "answer": "नवरा / पती", "hint": "Navra/Pati", "options": ["नवरा / पती", "बायको", "भाऊ", "बाबा"]},
        # --- Grammar & Sentences ---
        {"question": "How do you say 'I am hungry' in Marathi?", "answer": "मला भूक लागली आहे", "hint": "Mala bhook lagali aahe", "options": ["मला भूक लागली आहे", "मला झोप येत आहे", "मला तहान लागली आहे", "मला ताप आहे"]},
        {"question": "What does 'तुम्ही कसे आहात?' mean?", "answer": "How are you?", "hint": "A polite greeting", "options": ["How are you?", "What is your name?", "Where do you live?", "What do you do?"]},
        {"question": "What is 'Please' in Marathi?", "answer": "कृपया", "hint": "Kripaya", "options": ["कृपया", "धन्यवाद", "माफ करा", "नमस्कार"]},
        {"question": "What is 'Sorry' in Marathi?", "answer": "माफ करा", "hint": "Maaf kara", "options": ["माफ करा", "धन्यवाद", "कृपया", "ठीक आहे"]},
        {"question": "What does 'या' mean in Marathi?", "answer": "Please come", "hint": "An invitation", "options": ["Please come", "Please go", "Please sit", "Please wait"]},
        # --- Time & Days ---
        {"question": "What is 'Tomorrow' in Marathi?", "answer": "उद्या", "hint": "Udya", "options": ["उद्या", "काल", "आज", "परवा"]},
        {"question": "What is 'Monday' in Marathi?", "answer": "सोमवार", "hint": "Somvaar", "options": ["सोमवार", "मंगळवार", "शनिवार", "रविवार"]},
        {"question": "What is 'Morning' in Marathi?", "answer": "सकाळ", "hint": "Sakaal", "options": ["सकाळ", "दुपार", "संध्याकाळ", "रात्र"]},
        {"question": "What is 'Year' in Marathi?", "answer": "वर्ष", "hint": "Varsh", "options": ["वर्ष", "महिना", "आठवडा", "दिवस"]},
        {"question": "What is 'Hour' in Marathi?", "answer": "तास", "hint": "Taas", "options": ["तास", "मिनिट", "सेकंद", "दिवस"]},
        # --- Places ---
        {"question": "What is 'Hospital' in Marathi?", "answer": "रुग्णालय", "hint": "Rugnalaya", "options": ["रुग्णालय", "शाळा", "बाजार", "मंदिर"]},
        {"question": "What is 'Temple' in Marathi?", "answer": "मंदिर", "hint": "Mandir", "options": ["मंदिर", "मशीद", "चर्च", "रुग्णालय"]},
        {"question": "What is 'Library' in Marathi?", "answer": "ग्रंथालय", "hint": "Granthalaya", "options": ["ग्रंथालय", "शाळा", "कार्यालय", "बाजार"]},
        # --- Animals ---
        {"question": "What is 'Parrot' in Marathi?", "answer": "पोपट", "hint": "Popat", "options": ["पोपट", "कावळा", "चिमणी", "मोर"]},
        {"question": "What is 'Peacock' in Marathi?", "answer": "मोर", "hint": "Mor", "options": ["मोर", "पोपट", "कबूतर", "गरुड"]},
        {"question": "What is 'Cow' in Marathi?", "answer": "गाय", "hint": "Gaay", "options": ["गाय", "म्हैस", "शेळी", "मेंढी"]},
        {"question": "What is 'Tiger' in Marathi?", "answer": "वाघ", "hint": "Vaagh", "options": ["वाघ", "बिबट्या", "सिंह", "अस्वल"]},
        # --- Verbs ---
        {"question": "What is 'To eat' in Marathi?", "answer": "खाणे", "hint": "Khaane", "options": ["खाणे", "पिणे", "धावणे", "चालणे"]},
        {"question": "What is 'To sleep' in Marathi?", "answer": "झोपणे", "hint": "Jhopne", "options": ["झोपणे", "उठणे", "बसणे", "चालणे"]},
        {"question": "What is 'To speak' in Marathi?", "answer": "बोलणे", "hint": "Bolne", "options": ["बोलणे", "ऐकणे", "वाचणे", "लिहिणे"]},
        {"question": "What is 'To laugh' in Marathi?", "answer": "हसणे", "hint": "Hasne", "options": ["हसणे", "रडणे", "गाणे", "नाचणे"]},
        {"question": "What is 'To think' in Marathi?", "answer": "विचार करणे", "hint": "Vichaar karne", "options": ["विचार करणे", "पाहणे", "ऐकणे", "जाणवणे"]},
        # --- Adjectives ---
        {"question": "What is 'Beautiful' in Marathi?", "answer": "सुंदर", "hint": "Sundar", "options": ["सुंदर", "कुरूप", "विचित्र", "भयंकर"]},
        {"question": "What is 'Brave' in Marathi?", "answer": "शूर", "hint": "Shoor", "options": ["शूर", "भित्रा", "आळशी", "लोभी"]},
        {"question": "What is 'Fast' in Marathi?", "answer": "वेगाने", "hint": "Vegane", "options": ["वेगाने", "हळू", "लांब", "लहान"]},
        {"question": "What is 'Heavy' in Marathi?", "answer": "जड", "hint": "Jad", "options": ["जड", "हलका", "मोठा", "छोटा"]},
        # --- Culture & Proverbs ---
        {"question": "Marathi is primarily spoken in which Indian state?", "answer": "Maharashtra", "hint": "Land of Maratha warriors", "options": ["Maharashtra", "Gujarat", "Madhya Pradesh", "Rajasthan"]},
        {"question": "Marathi is written in which script?", "answer": "Devanagari", "hint": "Same as Hindi", "options": ["Devanagari", "Perso-Arabic", "Latin", "Gurmukhi"]},
        {"question": "What does 'हो' mean in Marathi?", "answer": "Yes", "hint": "An affirmative word", "options": ["Yes", "No", "Maybe", "Never"]},
        {"question": "What does 'नाही' mean in Marathi?", "answer": "No", "hint": "A negative word", "options": ["No", "Yes", "Maybe", "Always"]},
        {"question": "What is 'Rain' in Marathi?", "answer": "पाऊस", "hint": "Paaus", "options": ["पाऊस", "ऊन", "वारा", "बर्फ"]},
        {"question": "What is 'Sky' in Marathi?", "answer": "आकाश", "hint": "Aakaash", "options": ["आकाश", "जमीन", "पाणी", "जंगल"]},
        {"question": "What is 'Dream' in Marathi?", "answer": "स्वप्न", "hint": "Svapna", "options": ["स्वप्न", "झोप", "इच्छा", "आठवण"]},
        {"question": "What is 'Knowledge' in Marathi?", "answer": "ज्ञान", "hint": "Jnaan", "options": ["ज्ञान", "अज्ञान", "शिक्षण", "बुद्धी"]},
        {"question": "What is 'Peace' in Marathi?", "answer": "शांती", "hint": "Shaanti", "options": ["शांती", "युद्ध", "गोंधळ", "राग"]},
        {"question": "What is 'Victory' in Marathi?", "answer": "विजय", "hint": "Vijay", "options": ["विजय", "पराजय", "लढाई", "प्रयत्न"]},
        {"question": "What is 'Teacher' in Marathi?", "answer": "शिक्षक / गुरू", "hint": "Shikshak/Guru", "options": ["शिक्षक / गुरू", "विद्यार्थी", "डॉक्टर", "न्यायाधीश"]},
        {"question": "What is 'Freedom' in Marathi?", "answer": "स्वातंत्र्य", "hint": "Svaatantrya", "options": ["स्वातंत्र्य", "गुलामगिरी", "तुरुंग", "बंधन"]},
        {"question": "What is 'Language' in Marathi?", "answer": "भाषा", "hint": "Bhaasha", "options": ["भाषा", "शब्द", "अक्षर", "वाक्य"]},
        {"question": "What is 'Village' in Marathi?", "answer": "गाव", "hint": "Gaav", "options": ["गाव", "शहर", "जिल्हा", "राज्य"]},
        {"question": "What is 'Gold' in Marathi?", "answer": "सोने", "hint": "Sone", "options": ["सोने", "चांदी", "लोखंड", "तांबे"]},
        {"question": "What is 'Heart' in Marathi?", "answer": "हृदय", "hint": "Hrudaya", "options": ["हृदय", "मेंदू", "डोळा", "हात"]},
        {"question": "What is 'Road' in Marathi?", "answer": "रस्ता", "hint": "Rasta", "options": ["रस्ता", "पूल", "वाट", "शेत"]},
        {"question": "What is 'Market' in Marathi?", "answer": "बाजार", "hint": "Baazaar", "options": ["बाजार", "रुग्णालय", "शाळा", "ग्रंथालय"]},
        {"question": "What is 'Cloud' in Marathi?", "answer": "ढग", "hint": "Dhag", "options": ["ढग", "वारा", "पाऊस", "आकाश"]},
        {"question": "What is 'Star' in Marathi?", "answer": "तारा", "hint": "Taara", "options": ["तारा", "चंद्र", "सूर्य", "ढग"]},
    ],
}


def get_all_questions(language: str) -> list:
    """Return all questions for a given language."""
    return QUIZ_DB.get(language, QUIZ_DB.get("Hindi", []))


def get_random_question(language: str, exclude_indices: list = None) -> dict:
    """Return a random question, avoiding recently used ones."""
    import random
    pool = get_all_questions(language)
    if not pool:
        return {}
    if exclude_indices:
        available = [i for i in range(len(pool)) if i not in exclude_indices]
        if not available:
            available = list(range(len(pool)))  # Reset if all used
        idx = random.choice(available)
    else:
        idx = random.randint(0, len(pool) - 1)
    q = pool[idx].copy()
    q["_index"] = idx
    import random as _r
    options = q["options"][:]
    _r.shuffle(options)
    q["options"] = options
    return q


def get_total_count(language: str) -> int:
    """Return total number of questions for a language."""
    return len(QUIZ_DB.get(language, []))
