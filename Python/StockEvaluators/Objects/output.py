class Output:
    def __init__(self):
        self.messages = []  # List to store tuples of (message, status)

    def add(self, message: str, status: str = "neutral"):
        """
        Add a message with a status to the output.

        Args:
            message (str): The message to store.
            status (str): The status of the message ("success", "error", "neutral").
        """
        self.messages.append((message, status))
