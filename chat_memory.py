from collections import deque

class ChatMemory:
    """
    Maintains a sliding window memory buffer for the last N conversation turns.
    """
    def __init__(self, window_size=3):
        self.window_size = window_size
        self.buffer = deque(maxlen=window_size)

    def add_turn(self, user, bot):
        self.buffer.append((user, bot))

    def get_context(self):
        context = ""
        for user, bot in self.buffer:
            context += f"User: {user}\nBot: {bot}\n"
        return context
