# Best First Search
from queue import PriorityQueue
import time
import timeit


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.solution = [[' ' for _ in range(self.cols)]
                         for _ in range(self.rows)]
        self.step_count = 0

    def solve(self):
        start = (1, 1)
        end = (self.rows - 2, self.cols - 2)

        start_time = time.time()
        if self._best_first_search(start, end):
            end_time = time.time()
            self._print_solution()
            print("Langkah yang dibutuhkan:", self.step_count)
            # print("Waktu yang dibutuhkan:", end_time - start_time, "detik")
        else:
            print("Tidak ada solusi yang ditemukan.")

    def _best_first_search(self, start, end):
        queue = PriorityQueue()
        queue.put((0, start))
        visited = set([start])

        while not queue.empty():
            cost, current = queue.get()
            current_row, current_col = current

            if current == end:
                self._build_solution()
                return True

            neighbors = self._get_neighbors(current_row, current_col)

            for neighbor in neighbors:
                neighbor_row, neighbor_col = neighbor
                if neighbor not in visited:
                    priority = self._calculate_heuristic(neighbor, end)
                    queue.put((priority, neighbor))
                    visited.add(neighbor)
                    self.solution[neighbor_row][neighbor_col] = '*'
                    self.step_count += 1

        return False

    def _calculate_heuristic(self, current, end):
        current_row, current_col = current
        end_row, end_col = end
        return abs(end_row - current_row) + abs(end_col - current_col)

    def _get_neighbors(self, row, col):
        neighbors = []

        if row > 0 and self.maze[row - 1][col] != '#':
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and self.maze[row + 1][col] != '#':
            neighbors.append((row + 1, col))
        if col > 0 and self.maze[row][col - 1] != '#':
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and self.maze[row][col + 1] != '#':
            neighbors.append((row, col + 1))

        return neighbors

    def _build_solution(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == '#':
                    self.solution[row][col] = '#'
                elif self.solution[row][col] != '*':
                    self.solution[row][col] = ' '

        self.solution[1][1] = 'S'
        self.solution[self.rows - 2][self.cols - 2] = 'E'

    def _print_solution(self):
        for row in self.solution:
            print(' '.join(row))


def read_maze_from_file(file_path):
    maze = []
    with open(file_path, 'r') as file:
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
        file_path = input("Masukkan path file: ")
        maze = read_maze_from_file(file_path)
    else:
        print("Pilihan tidak valid.")
        return

    maze_solver = Maze(maze)

    execution_time = timeit.timeit(maze_solver.solve, number=1)
    # maze_solver.solve()
    print("Waktu yang dibutuhkan:", execution_time, "detik")


if __name__ == '__main__':
    main()


# Dalam kode di atas, program memberikan pilihan kepada pengguna untuk memasukkan labirin melalui keyboard atau membaca labirin dari file teks. Pengguna dapat memilih opsi yang diinginkan dengan memasukkan angka pilihan.
# - Jika pengguna memilih opsi 1, program akan meminta pengguna untuk memasukkan labirin baris per baris melalui keyboard.
# - Jika pengguna memilih opsi 2, program akan meminta pengguna untuk memasukkan path file teks yang berisi labirin.

# Setelah labirin diperoleh dari masukan pengguna, program akan memanggil metode `solve()` untuk menyelesaikan labirin menggunakan algoritma Best-First Search. Hasil solusi akan dicetak ke layar.

# Pastikan labirin yang dimasukkan sesuai dengan format yang diharapkan (misalnya, '#' untuk tembok, ' ' untuk jalur kosong, 'S' untuk titik awal, dan 'E' untuk titik akhir).
