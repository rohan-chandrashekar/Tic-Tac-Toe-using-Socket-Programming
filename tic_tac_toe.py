class TicTacToe:
    def __init__(self, player_symbol):
        self.symbol_list = [" "] * 9
        self.player_symbol = player_symbol

    def restart(self):
        self.symbol_list = [" "] * 9

    def draw_grid(self):
        print("\n       A   B   C\n")
        print(f"   1   {self.symbol_list[0]} ║ {self.symbol_list[1]} ║ {self.symbol_list[2]}")
        print("      ═══╬═══╬═══")
        print(f"   2   {self.symbol_list[3]} ║ {self.symbol_list[4]} ║ {self.symbol_list[5]}")
        print("      ═══╬═══╬═══")
        print(f"   3   {self.symbol_list[6]} ║ {self.symbol_list[7]} ║ {self.symbol_list[8]}\n")

    def edit_square(self, grid_coord):
        if grid_coord[0].isdigit():
            grid_coord = grid_coord[1] + grid_coord[0]
        col = grid_coord[0].capitalize()
        row = grid_coord[1]

        grid_index = -1
        mapping = {"A": 0, "B": 1, "C": 2}
        if col in mapping and row in "123":
            grid_index = (int(row) - 1) * 3 + mapping[col]

        if grid_index == -1:
            print("----INVALID INPUT----TURN SKIPPED---")
            return

        if self.symbol_list[grid_index] == " ":
            self.symbol_list[grid_index] = self.player_symbol
        else:
            print("----INVALID INPUT----TURN SKIPPED---")

    def update_symbol_list(self, new_symbol_list):
        self.symbol_list = new_symbol_list[:]

    def did_win(self, sym):
        g = self.symbol_list
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(g[a] == g[b] == g[c] == sym for a, b, c in wins)

    def is_draw(self):
        return " " not in self.symbol_list and not self.did_win("X") and not self.did_win("O")
