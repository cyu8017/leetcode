// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

func sumRemoteness(grid [][]int) int64 {
	m, n := len(grid), len(grid[0])
	seen := make([][]bool, m)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	var total int64
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != -1 {
				total += int64(grid[i][j])
			}
		}
	}
	var ans int64
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == -1 || seen[i][j] {
				continue
			}
			q := [][2]int{{i, j}}
			seen[i][j] = true
			var sum int64
			cnt := 0
			for len(q) > 0 {
				cur := q[0]
				q = q[1:]
				sum += int64(grid[cur[0]][cur[1]])
				cnt++
				for _, d := range dirs {
					ni, nj := cur[0]+d[0], cur[1]+d[1]
					if ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1 {
						seen[ni][nj] = true
						q = append(q, [2]int{ni, nj})
					}
				}
			}
			ans += (total - sum) * int64(cnt)
		}
	}
	return ans
}
