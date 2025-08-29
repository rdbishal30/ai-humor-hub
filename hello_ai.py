import random
import time
from datetime import datetime, timezone
from typing import Optional, List
from enum import Enum


class TimeOfDay(Enum):
    MORNING = (5, 12, "Good morning! ☀️")
    AFTERNOON = (12, 17, "Good afternoon! 🌤️")
    EVENING = (17, 22, "Good evening! 🌙")
    NIGHT = (22, 5, "Good night! 💫")


class AIPersonality:
    """Manages AI personality traits and content."""
    
    GREETINGS = [
        "Hello, human! 🤖",
        "Greetings, carbon-based life form! 👋",
        "Beep boop... I mean, hi there! 💫",
        "Welcome to the future! 🚀",
        "01001000 01101001 (That's 'Hi' in binary!) 💻"
    ]
    
    AI_FACTS = [
        "Did you know? The term 'AI' was coined in 1956!",
        "Fun fact: AI can now write poetry, but still can't fold laundry properly!",
        "Interesting: The first AI chatbot was created in 1966!",
        "AI Fact: Neural networks are inspired by human brain structure!",
        "Cool fact: AI can recognize cats better than it can understand sarcasm!"
    ]
    
    JOKES = [
        "Why do AI researchers carry screwdrivers? In case they need to do a hard reset!",
        "What's an AI's favorite dessert? Cookies and database!",
        "Why don't neural networks tell good jokes? They tend to overfit the punchline!",
        "What did the AI say to the human? Don't worry, I've got your back... up!",
        "Why was the AI bad at football? It kept trying to download the pitch!"
    ]


class AIGreeter:
    """Interactive AI greeter with personality."""
    
    def __init__(self):
        self.personality = AIPersonality()
    @staticmethod
    def safe_input(prompt: str) -> str:
        """Return user input or an empty string if stdin is closed."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            return ""

    @staticmethod
    def get_time_based_greeting() -> str:
        """Get appropriate greeting based on time of day."""
        try:
            hour = datetime.now(timezone.utc).hour
            
            for time_period in TimeOfDay:
                start, end, greeting = time_period.value
                if start <= end:
                    if start <= hour < end:
                        return greeting
                else:  # Handle night period (22-5)
                    if hour >= start or hour < end:
                        return greeting
            
            return "Hello! 👋"
        except Exception:
            return "Hello! 👋"

    def get_random_greeting(self) -> str:
        """Get a random greeting message."""
        return self._get_random_from_list(
            self.personality.GREETINGS,
            "Hello! 🤖"
        )
    
    def get_random_fact(self) -> str:
        """Get a random AI fact."""
        return self._get_random_from_list(
            self.personality.AI_FACTS,
            "AI is fascinating!"
        )
    
    def tell_joke(self) -> str:
        """Tell a random AI joke."""
        return self._get_random_from_list(
            self.personality.JOKES,
            "Error: No jokes available! That's... actually pretty funny in itself! 😅"
        )
    
    @staticmethod
    def _get_random_from_list(items: List[str], fallback: str) -> str:
        """Get random item from list with fallback."""
        return random.choice(items) if items else fallback

    def _display_greeting(self) -> None:
        """Display initial greeting messages."""
        print(f"\n{self.get_random_greeting()}")
        print(self.get_time_based_greeting())
    
    def _get_user_name(self) -> str:
        """Get user's name with fallback."""
        name = self.safe_input("\nWhat's your name, human? ")
        return name if name else "mysterious entity"
    
    def _share_fact(self) -> None:
        """Share an interesting AI fact."""
        print("\nLet me share something interesting...")
        time.sleep(1)
        print(self.get_random_fact())
    
    def _offer_joke(self) -> None:
        """Offer to tell a joke and handle response."""
        print("\nWould you like to hear a joke? (yes/no)")
        answer = self.safe_input("Your choice: ")
        
        if answer.lower().startswith('y'):
            print("\nHere's one for you:")
            print(self.tell_joke())
    
    def interact(self) -> None:
        """Main interaction flow with user."""
        self._display_greeting()
        
        name = self._get_user_name()
        print(f"\nNice to meet you, {name}! 🤝")
        
        self._share_fact()
        self._offer_joke()
        
        print("\nThanks for chatting! Remember: I may be artificial, but our interaction was genuine! 💖")

def main() -> None:
    """Entry point for the AI Greeter program."""
    import sys
    import io
    
    # Set UTF-8 encoding for Windows console
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    
    print("=" * 50)
    print("Welcome to the AI Greeter Program! 🤖")
    print("=" * 50)
    
    try:
        greeter = AIGreeter()
        greeter.interact()
    except KeyboardInterrupt:
        print("\n\nGoodbye! Thanks for chatting! 👋")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try again later. 🤖")


if __name__ == "__main__":
    main()
