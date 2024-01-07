"""File manager Module to operate data files"""
import json


class FileManager:
    """A Class representing a file manager."""

    def __init__(self, filename):
        """Initialize the file manager with a filename."""
        self.filename = filename

    def load_data(self):
        """Load data from a file."""
        try:
            with open(self.filename, "r", encoding="utf-8") as infile:
                try:
                    data = json.load(infile)
                except json.JSONDecodeError:
                    print(
                        f"The file {self.filename} is empty or does not contain valid JSON."
                    )
                    data = []
        except FileNotFoundError:
            print(f"The file {self.filename} is not found")
            print("Starting a New List")
            data = []
        return data

    def save_data(self, data):
        """Save data to a file."""
        with open(self.filename, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4)
