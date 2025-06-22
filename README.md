# ai-career-guide-chatbot

An AI-powered personalized career guidance tool for O-Level/A-Level students in Pakistan, built with Python and Streamlit.


```
# 🎓 AI-Powered Career Guide Chatbot for O/A Level Students (Pakistan)

## Project Overview

The **AI-Powered Career Guide Chatbot** is an innovative tool designed to provide personalized academic and career counseling for students in Pakistan who have completed their O-Levels, A-Levels, or equivalent (like F.Sc/ICS). Navigating higher education and career choices can be daunting; this chatbot aims to simplify that process by offering data-driven, AI-generated guidance tailored to each student's unique profile.

By inputting their academic background, interests, strengths, and career aspirations, students can receive recommendations for suitable Bachelor's degrees offered in Pakistani universities, potential career paths within the local job market, and essential skills required for success. This project seeks to democratize access to quality career guidance, empowering Pakistani youth to make informed decisions about their future.

## Key Features

-   **Personalized Degree Recommendations**: Suggests relevant Bachelor's degrees based on academic performance (simulated), subjects, and interests.
-   **Pakistan-Specific Career Paths**: Outlines potential career trajectories within the context of Pakistan's evolving job market.
-   **Skill Gap Identification**: Highlights key technical and soft skills needed for recommended fields.
-   **Interactive Web GUI**: Built with Streamlit for a user-friendly, web-based interface accessible via a browser.
-   **AI-Powered Guidance**: Leverages the Google Gemini API (`gemini-2.0-flash`) for intelligent analysis and generation of comprehensive advice.
-   **Secure API Key Management**: Uses `.env` files for safe handling of sensitive API keys.
-   **Automatic Project Setup**: The PowerShell script quickly sets up the required project directory structure and placeholder files.

## How It Works

1.  **Student Profile Input**: Through the Streamlit GUI (`app.py`), students input their O/A Level (or equivalent) subjects, grades, interests, strengths, and career goals.
2.  **API Key Loading**: The application securely loads the Google API key from the `.env` file.
3.  **Prompt Engineering**: The `CareerGuideGenerator` (`src/core/generator.py`) constructs a detailed prompt based on the student's profile, asking the Gemini model to act as an expert career counselor for Pakistani students.
4.  **Gemini API Interaction**: An HTTP POST request is made to the Google Gemini API (`gemini-2.0-flash`) to get the AI-generated guidance.
5.  **AI-Generated Guidance**: The Gemini model processes the prompt and returns personalized recommendations for degrees, career paths, and skills.
6.  **Display Output**: The guidance is presented clearly in the Streamlit interface, offering actionable insights to the student.
7.  **Directory Management**: Utility functions (`src/utils/file_operations.py`) ensure that project directories are correctly structured.

## Project Structure


```

ai-career-guide-chatbot/

├── .env                  # Environment variables (e.g., API keys - already existing, not created by script)

├── src/                  # Source code directory

│   ├── init.py       # Makes 'src' a Python package

│   ├── core/             # Core logic for AI generation

│   │   ├── init.py

│   │   ├── generator.py  # Contains the CareerGuideGenerator class and API integration

│   │   └── config.py     # Global configuration (optional)

│   └── utils/            # Utility functions

│       ├── init.py

│       └── file_operations.py # Utility for directory creation

├── app.py                # Main Streamlit application entry point (GUI)

├── main.py               # Optional: Command-line interface (CLI) entry point/backend processing

├── requirements.txt      # Python dependencies

└── README.md             # Project documentation (this file)

```

## Setup and Installation

1.  **Create GitHub Repository (Already Done):**
    You have already used GitHub Desktop to create and clone your repository (`ai-career-guide-chatbot`).

2.  **Open in VS Code & Run Setup Script:**
    Open the cloned repository folder in VS Code. Open the PowerShell terminal within VS Code and **navigate into your `ai-career-guide-chatbot` directory**. Then, run the provided setup script (the PowerShell command block above). This script will create all necessary folders and placeholder files within your existing repository, but **it will NOT create or modify your `.env` file, nor will it interfere with your `.git` or `.gitignore` files.**

3.  **Copy Code into Files:**
    Copy the code provided in separate blocks below (for `.env` if needed, and for `requirements.txt`, `app.py`, `main.py`, and all files under `src/`) and paste them into their respective files in your project directory.

4.  **Create and Activate a Python Virtual Environment (Recommended):**
    In your project's root directory (`ai-career-guide-chatbot`), run:
    ```bash
    python -m venv venv
    ```
    * **Activate the virtual environment:**
        * On Windows:
            ```bash
            .\venv\Scripts\activate
            ```
        * On macOS/Linux:
            ```bash
            source venv/bin/activate
            ```

5.  **Install Dependencies:**
    With your virtual environment activated:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Verify Google API Key in .env:**
    Ensure your `.env` file (which you already have) in the `ai-career-guide-chatbot/` root directory contains your API key correctly set:
    ```
    API_KEY=YOUR_GOOGLE_API_KEY_HERE
    ```
    **Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual API key.**

## Usage

1.  **Run the Streamlit application:**
    Ensure your virtual environment is active, then from the `ai-career-guide-chatbot/` directory, run:
    ```bash
    streamlit run app.py
    ```
    This will open the web-based GUI for your AI Career Guide in your default web browser.

## Future Enhancements (Ideas for Expansion)

-   **University Database Integration**: Connect to a more comprehensive (simulated or real, if available) database of Pakistani universities, their programs, and admission criteria.
-   **Interactive Q&A Sessions**: Implement a more robust conversational AI for follow-up questions about specific fields or universities.
-   **Personality Assessment Integration**: Incorporate simple psychological tests to better align recommendations with student's innate preferences.
-   **Job Market Data Visualization**: Integrate (simulated) real-time job market data and salary trends for recommended careers in Pakistan.
-   **Success Stories/Mentorship**: Feature anonymized success stories or pathways to connect with mentors in desired fields.
-   **Multi-language Support**: Offer guidance in Urdu and other regional languages for broader accessibility.

```
