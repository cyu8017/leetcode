// LeetCode 2923 - Find Champion I
// https://leetcode.com/problems/find-champion-i/

func findChampion(grid [][]int) int {
	n := len(grid)
	for i := 0; i < n; i++ {
		win := true
		for j := 0; j < n; j++ {
			if i != j && grid[i][j] == 0 {
				win = false
				break
			}
		}
		if win {
			return i
		}
	}
	return -1
}
