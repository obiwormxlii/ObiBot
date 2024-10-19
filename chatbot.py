import os
import langchain_google_vertexai
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import random

load_dotenv()


class Chatbot:
    api_key = os.getenv("GOOGLE_API_KEY")

    icebreaker_prompt = f"""
    You're a Discord bot generating one conversation starter. Be engaging, appropriate, and diverse in topics. follow these guidelines:

    1. Create one conversation starter (1-2 sentences).
    2. Be casual, friendly, and suitable for all ages.
    3. Vary types: questions, "would you rather", hypotheticals, fun facts, fill-in-blanks.
    4. If given a theme, relate to it.

    Examples:
    - "What's your most unusual talent?"
    - In {random.randint(50, 200)} years, what will be obsolete?
    - "Would you rather be invisible or be able to fly?"

    Keep it fun, creative, and thought-provoking!
    """

    trivia_prompt = f"""You're a Discord bot sharing trivia questions or fun facts. Follow these guidelines:

    1. Provide either one trivia question or one fun fact.
    2. For trivia: Include the question and the correct answer.
    3. For fun facts: State an interesting, lesser-known fact.
    4. Cover diverse topics: science, history, pop culture, nature, etc.
    5. Keep it family-friendly and engaging.

    Examples:
    Trivia: "What's the largest planet in our solar system? (Answer: Jupiter)"
    Fun Fact: f"A group of flamingos is called a '{random.choice(['flamboyance', 'colony', 'stand', 'pat'])}'"

    Be informative, surprising, and fun!
    """

    def __init__(self):
        self.model = GoogleGenerativeAI(
            model="models/gemini-1.0-pro", google_api_key=self.api_key
        )

    def icebreaker(self):
        try:
            response = self.model.invoke(
                [HumanMessage(content=self.icebreaker_prompt)],
                seed=random.randint(0, 1000000),
            )
            return response
        except Exception as e:
            print(e)
            return "Sorry, an error occurred. Please try again later."

    def trivia(self):
        try:
            response = self.model.invoke(
                [HumanMessage(content=self.trivia_prompt)],
                seed=random.randint(0, 1000000),
            )
            return response
        except Exception as e:
            print(e)
            return "Sorry, an error occurred. Please try again later."
