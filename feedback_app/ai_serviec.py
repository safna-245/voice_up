from google import genai

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

client = genai.Client(api_key=api_key)


def analyze_feedback(feedback_text):

    prompt = f"""
        You are an expert campus feedback analyzer.

        Analyze the following student feedback:

        Feedback: {feedback_text}

        Perform these two tasks:

        1. Sentiment Analysis:
           Classify the sentiment as one of:
           positive, negative, neutral, unknown.

        2. Category Classification:
           Classify the feedback into one of:
           faculty, academics, infrastructure,
           administration, facilities, other.

        Return the result in JSON format only:

        {{
            "sentiment": "positive",
            "category": "faculty"
        }}

        Do not include explanations or markdown.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text