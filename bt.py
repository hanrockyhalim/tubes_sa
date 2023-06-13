# Backtracking
import timeit

import time


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.solution_backtracking = [
            [' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.step_count = 0

    def solve_backtracking(self):
        start = (1, 1)
        end = (self.rows - 2, self.cols - 2)

        # start_time = time.time()
        if self._backtrack(start, end, self.solution_backtracking):
            # end_time = time.time()
            self._print_solution(self.solution_backtracking)
            print("Langkah yang dibutuhkan:", self.step_count)
            # print("Waktu yang dibutuhkan:", end_time - start_time, "detik")
        else:
            print("Tidak ada solusi Backtracking yang ditemukan.")

    def _backtrack(self, current, end, solution):
        current_row, current_col = current

        if current == end:
            self._build_solution(solution)
            return True

        if self._is_valid_move(current_row, current_col):
            solution[current_row][current_col] = '0'
            self.step_count += 1

            if self._backtrack((current_row, current_col + 1), end, solution):
                return True

            if self._backtrack((current_row + 1, current_col), end, solution):
                return True

            if self._backtrack((current_row - 1, current_col), end, solution):
                return True

            if self._backtrack((current_row, current_col - 1), end, solution):
                return True

            solution[current_row][current_col] = ' '
            self.step_count -= 1

        return False

    def _is_valid_move(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.maze[row][col] == '#':
            return False
        return True

    def _build_solution(self, solution):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == '#':
                    solution[row][col] = '#'
                elif solution[row][col] != '0':
                    solution[row][col] = ' '

        solution[1][1] = 'S'
        solution[self.rows - 2][self.cols - 2] = 'E'

    def _print_solution(self, solution):
        for row in solution:
            print(' '.join(row))


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

    # maze_solver.solve_backtracking()

    print("Waktu yang dibutuhkan:", execution_time, "detik")


if __name__ == '__main__':
    main()
