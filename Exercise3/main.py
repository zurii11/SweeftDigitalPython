def main():
    def bomberMan(n, grid):
        print(r)
        if n == 1:
            return grid

        if n % 2 == 0:
            return ['O'*c for i in range(r)]

        n //= 2 

        for j in range((n+1) % 2 + 1):
            print(r)
            print(c)
            print(n)
            new_grid = [['O']*c for i in range(r)]
            print(new_grid)
            def set(x, y):
                if 0 <= x < r and 0 <= y < c:
                    new_grid[x][y] = '.'

            xi = [0, 0, 0, 1, -1]
            yi = [0, -1, 1, 0, 0]

            for x in range(r):
                for y in range(c):
                    if grid[x][y] == 'O':
                        for i, q in zip(xi, yi):
                            set(x+i, y+q)

            grid = new_grid
            print(new_grid)

        return ["".join(x) for x in grid]

    output = open("output", 'w')
    f = open("input", 'r')
    lines = f.readlines()
    grid_items = lines[1:]
    firstLine = lines[0].split()

    r = int(firstLine[0])
    c = int(firstLine[1])
    n = int(firstLine[2])
    print(r)
    print(c)
    print(n)

    grid = []

    for i in range(r):
        grid_item = grid_items[i]
        grid.append(grid_item)

    print(bomberMan(n, grid))
    result = bomberMan(n, grid)

    output.write('\n'.join(result))
    output.write('\n')
    output.close()

if __name__ == "__main__":
    main()
    
