import timeit

class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.best_solution = None
        self.step_count = 0

    def solve_backtracking(self):
        start = (1, 1)
        end = (self.rows - 2, self.cols - 2)

        if self._backtrack(start, end, []):
            self._build_best_solution()
            self._print_solution(self.best_solution)
            print("Langkah yang dibutuhkan:", self.step_count)
        else:
            print("Tidak ada solusi Backtracking yang ditemukan.")

    def _backtrack(self, current, end, solution):
        if current == end:
            self.solution = solution
            return True

        current_row, current_col = current

        if self._is_valid_move(current_row, current_col):
            solution.append(current)
            self.step_count += 1

            # Check right
            next_position = (current_row, current_col + 1)
            if next_position not in solution:
                if self._backtrack(next_position, end, solution):
                    return True

            # Check down
            next_position = (current_row + 1, current_col)
            if next_position not in solution:
                if self._backtrack(next_position, end, solution):
                    return True

            # Check up
            next_position = (current_row - 1, current_col)
            if next_position not in solution:
                if self._backtrack(next_position, end, solution):
                    return True

            # Check left
            next_position = (current_row, current_col - 1)
            if next_position not in solution:
                if self._backtrack(next_position, end, solution):
                    return True

            # solution.pop()
            # self.step_count -= 1

        return False

    def _is_valid_move(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.maze[row][col] == '#':
            return False
        return True

    def _build_best_solution(self):
        self.best_solution = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for row, col in self.solution:
            self.best_solution[row][col] = '0'
        self.best_solution[1][1] = 'S'
        self.best_solution[self.rows - 2][self.cols - 2] = 'E'

    def _print_solution(self, solution):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell == '#':
                    print('#', end=' ')
                else:
                    print(solution[i][j], end=' ')
            print()


def read_maze_from_file(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            maze.append(list(line))
    return maze


def read_maze_from_keyboard():
    maze = []
    print("Masukkan labirin (tekan Enter setelah setiap baris, selesai dengan Enter kosong):")
    while True:
        line = input()
        if line:
            maze.append(list(line))
        else:
            break
    return maze


def main():
    print("Pilih sumber masukan:")
    print("1. Masukkan labirin melalui keyboard")
    print("2. Baca labirin dari file teks")
    choice = input("Pilihan: ")

    if choice == '1':
        maze = read_maze_from_keyboard()
    elif choice == '2':
        filename = input("Masukkan nama file: ")
        maze = read_maze_from_file(filename)
    else:
        print("Pilihan tidak valid.")
        return

    maze_solver = Maze(maze)
    print("Solusi Backtracking:")

    execution_time = timeit.timeit(maze_solver.solve_backtracking, number=1)

    print("Waktu yang dibutuhkan:", execution_time, "detik")


if __name__ == '__main__':
    main()
