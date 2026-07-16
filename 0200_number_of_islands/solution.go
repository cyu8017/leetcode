// LeetCode 0200 - Number of Islands
// https://leetcode.com/problems/number-of-islands/

func numIslands(grid [][]byte) int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return 0
    }

    var flood func(int, int)
    flood = func(row, col int) {
        if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[row]) || grid[row][col] != '1' {
            return
        }
        grid[row][col] = '0'
        flood(row+1, col)
        flood(row-1, col)
        flood(row, col+1)
        flood(row, col-1)
    }

    islands := 0
    for row := range grid {
        for col := range grid[row] {
            if grid[row][col] == '1' {
                islands++
                flood(row, col)
            }
        }
    }
    return islands
}
