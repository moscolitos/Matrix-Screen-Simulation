# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:20:11 2023

@author: Mosco
"""

# Import necessary modules
import tkinter as tk
import random
from enum import Enum

# Define Enumeration class for Character Type
class CharacterType(Enum):
    """Enumeration class for character type."""
    ZERO = 0
    ONE = 1
    SPACE = 2
    SPECIAL = 3

class MatrixScreen:
    """Class to create a Matrix-like screen using tkinter."""

    def __init__(self, update_interval=100, line_length=189):
        """
        Initializes the MatrixScreen class with update_interval and line_length parameters.
        
        Args:
            update_interval (int): The time interval for screen updates.
            line_length (int): The number of characters in each line on the screen.
        """
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Matrix Screen")
        self.root.geometry("1920x1080")
        self.root.configure(bg="black")

        # Create a list of special characters
        self.special_characters = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

        # Create the Matrix display
        self.matrix_display = tk.Text(
            self.root,
            bg="black",
            fg="green",
            font=("Courier", 12),
            wrap=tk.WORD,
            padx=10,
            pady=10,
        )
        self.matrix_display.pack(expand=True, fill=tk.BOTH)

        # Set the update interval and line length
        self.update_interval = update_interval
        self.line_length = line_length

    def random_char(self):
        """
        Returns a random character: '0', '1', ' ' or a special character.
        
        Returns:
            str: A random character.
        """
        choice = CharacterType(random.randint(0, 3))
        if choice == CharacterType.ZERO:
            return '0'
        elif choice == CharacterType.ONE:
            return '1'
        elif choice == CharacterType.SPACE:
            return ' '
        else:
            return random.choice(self.special_characters)

    def update_matrix(self):
        """
        Updates the Matrix display and schedules the next update.
        """
        # Generate new line
        new_line = ''.join([self.random_char() for _ in range(self.line_length)])
        self.matrix_display.insert(tk.END, new_line + '\n')
        self.matrix_display.see(tk.END)

        # Schedule the next update
        self.root.after(self.update_interval, self.update_matrix)

if __name__ == "__main__":
    # Create an instance of the MatrixScreen class
    matrix = MatrixScreen()
    # Start updating the Matrix display
    matrix.update_matrix()
    # Run the tkinter main loop
    matrix.root.mainloop()
