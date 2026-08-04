// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

func findFarmland(land [][]int) [][]int {
	m, n := len(land), len(land[0])
	ans := [][]int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if land[i][j] == 1 && (i == 0 || land[i-1][j] == 0) && (j == 0 || land[i][j-1] == 0) {
				r, c := i, j
				for r+1 < m && land[r+1][j] == 1 {
					r++
				}
				for c+1 < n && land[i][c+1] == 1 {
					c++
				}
				ans = append(ans, []int{i, j, r, c})
			}
		}
	}
	return ans
}
