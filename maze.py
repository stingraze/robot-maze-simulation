def dfs(maze):
    step_counter = 1  # Global step counter for all moves (forward and backtracking)

    def find_start():
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'S':
                    return (i, j)
        return None  # In case there's no 'S' in the maze

    def is_valid(x, y):
        return (0 <= x < len(maze) and 
                0 <= y < len(maze[0]) and 
                maze[x][y] not in ('1', '#'))

    def solve_dfs(x, y, path):
        nonlocal step_counter
        
        # 1) Record stepping *into* position (x, y)
        print(f"Step {step_counter}: Entering cell ({x}, {y}) with path so far: {path}")
        step_counter += 1
        
        path.append((x, y))  # Add current cell to the path

        # 2) Check if we've reached the end
        if maze[x][y] == 'E':
            print("Reached the exit! Full path:", path)
            return True

        # 3) Mark the current cell as visited to avoid revisiting
        original_value = maze[x][y]
        maze[x][y] = '#'
        
        # 4) Explore all four directions
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                if solve_dfs(new_x, new_y, path):
                    return True

        # 5) If we are here, we could not find a path through (x, y). Backtrack.
        maze[x][y] = original_value  # Unmark this cell (restore original value)
        path.pop()                   # Remove from the current path
        
        print(f"Step {step_counter}: Backtracking from cell ({x}, {y}). Current path: {path}")
        step_counter += 1
        
        return False

    start = find_start()
    if start is None:
        print("No start ('S') found in the maze.")
        return
    
    start_x, start_y = start
    found_path = solve_dfs(start_x, start_y, [])
    if not found_path:
        print("No path found.")

# Example usage
maze_example = [
    ['S', 0,   1,   0],
    [0,   0,   1,   0],
    [1,   0,   0,   0],
    [1,   1,   1,  'E']
]
dfs(maze_example)
