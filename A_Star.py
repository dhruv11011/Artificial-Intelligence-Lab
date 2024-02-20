def manhattan_dist(puzzle, goal):
    distance = 0
    for i in range(9):
        x, y = divmod(i, 3)
        x_goal, y_goal = divmod(goal.index(puzzle[i]), 3)
        distance += abs(x - x_goal) + abs(y - y_goal)
    return distance

def a_star(start, goal):
    open_list = [(0, start, [])]
    closed_list = []

    while open_list:
        (f, puzzle, path) = min(open_list, key=lambda x: x[0] + manhattan_dist(x[1], goal))
        open_list.remove((f, puzzle, path))
        closed_list.append((f, puzzle, path))

        if puzzle == goal:
            return (path + [goal], f)

        zero_index = puzzle.index(0)
        x, y = divmod(zero_index, 3)
        neighbors = [(x + i, y + j) for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        for (x_neighbor, y_neighbor) in neighbors:
            if 0 <= x_neighbor < 3 and 0 <= y_neighbor < 3:
                puzzle_copy = puzzle.copy()
                index_neighbor = 3 * x_neighbor + y_neighbor
                puzzle_copy[zero_index], puzzle_copy[index_neighbor] = puzzle_copy[index_neighbor], puzzle_copy[zero_index]
                if (f + 1, puzzle_copy, path + [puzzle]) not in closed_list:
                    open_list.append((f + 1, puzzle_copy, path + [puzzle]))

def print_puzzle(puzzle):
            for i in range(9):
                x, y = divmod(i, 3)
                print(puzzle[i], end=" ")
                if y == 2:
                    print(" ")

start =[2,8,3,1,6,4,7,0,5]
goal=[1,2,3,8,0,4,7,6,5]

result = a_star(start, goal)
if result:
        (path, cost) = result
        for puzzle in path:
            print_puzzle(puzzle)
            print("")
        print("Total cost:", cost)
else:
        print("No solution found")
