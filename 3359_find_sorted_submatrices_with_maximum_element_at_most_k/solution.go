// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

func countSortedMatrices(grid [][]int, k int) int64 {
	m, n := len(grid), len(grid[0])
	var ans int64
	for r1 := 0; r1 < m; r1++ {
		for r2 := r1; r2 < m; r2++ {
			for c1 := 0; c1 < n; c1++ {
				for c2 := c1; c2 < n; c2++ {
					ok := true
					mx := grid[r1][c1]
					for i := r1; i <= r2 && ok; i++ {
						for j := c1; j <= c2; j++ {
							if grid[i][j] > k {
								ok = false
								break
							}
							if grid[i][j] > mx {
								mx = grid[i][j]
							}
							if j > c1 && grid[i][j] < grid[i][j-1] {
								ok = false
								break
							}
							if i > r1 && grid[i][j] < grid[i-1][j] {
								ok = false
								break
							}
						}
					}
					if ok {
						ans++
					}
				}
			}
		}
	}
	return ans
}
