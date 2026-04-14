# Social Media Activity Monitoring App

A cross-platform mobile app that lets you monitor and analyze social media activity on platforms like Instagram, Reddit, and Telegram. Built as a college project to explore how publicly available data from social media can be used for safety and awareness purposes.

## What does it do?

The idea behind this project is simple — given a social media account, can we extract useful insights from it? Things like:

- **Phone numbers** mentioned across posts, bios, and comments
- **Hashtags** being used frequently (and whether they're offensive)
- **Locations** mentioned in captions and comments
- **Offensive language detection** in bios and comments using a trained ML model
- **Profile details** like follower/following count, profile picture, and post images

The app currently supports **Instagram** monitoring with a working backend, and has UI screens for **Reddit** (subreddit tracking and post URL analysis) and **Telegram** as well.

## How it works

### Frontend (Flutter)
The mobile app is built with **Flutter** and runs on Android, iOS, Windows, macOS, Linux, and Web. It has:
- A splash screen on launch
- A home screen where you pick the platform (Instagram / Reddit / Telegram)
- For Instagram — you log in with credentials, and it fetches a detailed profile report
- For Reddit — you can track a subreddit or analyze a specific post by URL
- A clean report screen showing all extracted data in tables

### Backend (Python - FastAPI)
The backend is a **FastAPI** server that handles all the heavy lifting:
- Uses **Instaloader** to log into Instagram and scrape profile data (posts, comments, bio, tagged posts)
- Extracts phone numbers, hashtags, and locations using **regex** and **spaCy NLP**
- Runs an **ML-based hate speech classifier** (Logistic Regression + TF-IDF) to flag offensive content
- Serves everything via REST API endpoints that the Flutter app calls
- Has a separate **Flask app** for a web-based offensive language detector using an SVM model

### Machine Learning
- Trained a **Logistic Regression** classifier on a Twitter hate speech dataset (~25k tweets)
- Uses **TF-IDF vectorization** for feature extraction
- Also has an **SVM model** for the web-based detector
- The model classifies text as offensive or non-offensive in real time
- OCR support via **Tesseract** for extracting text from images

## Project Structure

```
├── activity_monitoring_of_any_person/    # Flutter mobile app
│   ├── lib/
│   │   ├── main.dart                     # App entry point
│   │   ├── pages/
│   │   │   ├── first.dart                # Splash screen
│   │   │   ├── second.dart               # Home screen (platform selection)
│   │   │   ├── insta.dart                # Instagram login flow
│   │   │   └── data.dart                 # Profile report screen
│   │   ├── reddit pages/
│   │   │   └── options.dart              # Reddit tracking options
│   │   └── backend/
│   │       ├── main.py                   # FastAPI backend server
│   │       ├── training.py               # ML model training script
│   │       └── testing.py                # Text classification helper
│   └── pubspec.yaml
│
├── BACKEND/
│   ├── INSTAGRAM/
│   │   ├── app.py                        # Flask web app for offensive language detection
│   │   ├── main.py                       # Alternative backend server
│   │   ├── img_text_extract.py           # OCR text extraction from images
│   │   ├── SVM_model.pkl                 # Trained SVM model
│   │   ├── vec_model.pkl                 # TF-IDF vectorizer for SVM
│   │   └── labeled_data.csv              # Training dataset
│   ├── REDDIT/
│   └── TELEGRAM/
│
└── Offensive_Language_Detector-main/     # Jupyter notebook for model experimentation
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Mobile App | Flutter (Dart) |
| Backend API | FastAPI (Python) |
| Web App | Flask (Python) |
| ML Models | Scikit-learn (Logistic Regression, SVM) |
| NLP | spaCy, TF-IDF Vectorizer |
| Scraping | Instaloader, PRAW (Reddit) |
| OCR | Tesseract (pytesseract) |

## Setup & Running

### Prerequisites
- Flutter SDK installed
- Python 3.8+
- Tesseract OCR installed (for image text extraction)

### Backend
```bash
cd activity_monitoring_of_any_person/lib/backend
pip install fastapi uvicorn instaloader spacy scikit-learn joblib praw requests
python -m spacy download en_core_web_sm
python main.py
```
The API server will start on `http://0.0.0.0:5200`

### Flutter App
```bash
cd activity_monitoring_of_any_person
flutter pub get
flutter run
```

> **Note:** Make sure to update the IP address in the Dart files (`insta.dart`, `data.dart`, `options.dart`) to match your local machine's IP so the app can talk to the backend.

## Important Disclaimers

- This project was built for **educational purposes only**
- Scraping Instagram data may violate their Terms of Service — use at your own risk
- The app shows a warning popup before any Instagram login to make users aware of potential account risks
- Please respect other people's privacy when using this tool

## Future Scope

- Add full Telegram monitoring support
- Improve the ML model accuracy with a larger dataset
- Add sentiment analysis alongside offensive language detection
- Build a dashboard for visualizing trends over time
- Support for more platforms (Twitter/X, Facebook, etc.)
