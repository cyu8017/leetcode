// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

func findShortestPath(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    sr, sc := 0, 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == -1 {
                sr, sc = i, j
            }
        }
    }
    dirs := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    dist := make([][]int, m)
    for i := range dist {
        dist[i] = make([]int, n)
        for j := range dist[i] {
            dist[i][j] = -1
        }
    }
    queue := [][2]int{{sr, sc}}
    dist[sr][sc] = 0
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        r, c := cur[0], cur[1]
        if grid[r][c] == 2 {
            return dist[r][c]
        }
        for _, d := range dirs {
            nr, nc := r+d[0], c+d[1]
            if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0 && dist[nr][nc] < 0 {
                dist[nr][nc] = dist[r][c] + 1
                queue = append(queue, [2]int{nr, nc})
            }
        }
    }
    return -1
}
