import random
import time
from datetime import datetime
import os

class AIGreeter:
    def __init__(self):
        self.greetings = [
            "Hello, human! 🤖",
            "Greetings, carbon-based life form! 👋",
            "Beep boop... I mean, hi there! 💫",
            "Welcome to the future! 🚀",
            "01001000 01101001 (That's 'Hi' in binary!) 💻"
        ]
        
        self.ai_facts = [
            "Did you know? The term 'AI' was coined in 1956!",
            "Fun fact: AI can now write poetry, but still can't fold laundry properly!",
            "Interesting: The first AI chatbot was created in 1966!",
            "AI Fact: Neural networks are inspired by human brain structure!",
            "Cool fact: AI can recognize cats better than it can understand sarcasm!"
        ]
    def safe_input(self, prompt: str) -> str:
        """Return user input or an empty string if stdin is closed."""
        try:
            return input(prompt)
        except EOFError:
            return ""

    def get_time_based_greeting(self):
        # Use local time but with better timezone awareness
        # Note: This uses system local time. In production environments,
        # consider using timezone-aware datetime or pytz for consistent behavior
        try:
            hour = datetime.now().hour
        except Exception:
            # Fallback if there are any datetime issues
            return "Hello! 👋"
            
        if 5 <= hour < 12:
            return "Good morning! ☀️"
        elif 12 <= hour < 17:
            return "Good afternoon! 🌤️"
        elif 17 <= hour < 22:
            return "Good evening! 🌙"
        else:
            return "Good night! 💫"

    def tell_joke(self):
        jokes = [
            "Why do AI researchers carry screwdrivers? In case they need to do a hard reset!",
            "What's an AI's favorite dessert? Cookies and database!",
            "Why don't neural networks tell good jokes? They tend to overfit the punchline!",
            "What did the AI say to the human? Don't worry, I've got your back... up!",
            "Why was the AI bad at football? It kept trying to download the pitch!"
        ]
        if not jokes:
            return "Error: No jokes available! That's... actually pretty funny in itself! 😅"
        return random.choice(jokes)

    def interact(self):
        greeting = random.choice(self.greetings) if self.greetings else "Hello! 🤖"
        print(f"\n{greeting}")
        print(f"{self.get_time_based_greeting()}")
        
        name = self.safe_input("\nWhat's your name, human? ")
        if not name:
            name = "mysterious entity"
        print(f"\nNice to meet you, {name}! 🤝")
        
        print("\nLet me share something interesting...")
        time.sleep(1)
        fact = random.choice(self.ai_facts) if self.ai_facts else "AI is fascinating!"
        print(fact)
        
        print("\nWould you like to hear a joke? (yes/no)")
        answer = self.safe_input("Your choice: ")
        if answer.lower().startswith('y'):
            print("\nHere's one for you:")
            print(self.tell_joke())
        
        print("\nThanks for chatting! Remember: I may be artificial, but our interaction was genuine! 💖")

if __name__ == "__main__":
    print("=" * 50)
    print("Welcome to the AI Greeter Program! 🤖")
    print("=" * 50)
    
    ai = AIGreeter()
    ai.interact()
