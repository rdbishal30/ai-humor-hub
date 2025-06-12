import random

def generate_funny_drawing():
    """Generates a simple text-based funny drawing."""
    drawings = [
        r"""
          /\_/\
         ( o.o )
          > ^ <
        """,
        r"""
         .--.
        |o_o |
        |:_/ |
       //   \ \
      (|     | )
     /'\_   _/`\
     \___)=(___/
        """,
        r"""
         .--""--.
        /        \
       |  O  O  |
       |   \/   |
        \  --  /
         '.__.'
        """,
        r"""
        (\(\
        ( -.-)
        o_(")(")
        """
    ]
    return random.choice(drawings)

if __name__ == "__main__":
    print(generate_funny_drawing())
