#!/usr/bin/python3

import random
import os


def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    """A class to represent a Minesweeper game."""

    def __init__(self, width=10, height=10, mines=10):
        """
        Initializes a Minesweeper game.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            mines (int): The number of mines on the board.
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.mines_left = mines
        self.safe_cells = width * height - mines

    def print_board(self, reveal=False):
        """
        Prints the Minesweeper board to the console.

        Args:
            reveal (bool): If True, reveals all cells (for game over/win).
        """
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(f"Mines Left: {self.mines_left}")

    def count_mines_nearby(self, x, y):
        """
        Counts the number of mines adjacent to a given cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            int: The number of adjacent mines.
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # Skip the cell itself
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Reveals a cell on the board.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            bool: True if the reveal was successful, False if a mine was hit.
        """
        if self.game_over:
            return True
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        if self.revealed[y][x]:
            return True
        if (y * self.width + x) in self.mines:
            self.game_over = True
            return False

        self.revealed[y][x] = True
        self.safe_cells -= 1

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    self.reveal(nx, ny)

        return True

    def check_win(self):
        """
        Checks if the player has won the game.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        if self.safe_cells == 0:
            self.print_board(reveal=True)
            print("Congratulations! You won!")
            self.game_over = True
            return True
        return False

    def play(self):
        """Plays the Minesweeper game."""
        while not self.game_over:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid input. Coordinates out of range.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_win():
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
