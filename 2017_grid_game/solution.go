// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

func gridGame(grid [][]int) int64 {
	n := len(grid[0])
	var top, bottom, ans int64
	for _, v := range grid[0] {
		top += int64(v)
	}
	ans = 1<<63 - 1
	for i := 0; i < n; i++ {
		top -= int64(grid[0][i])
		cur := top
		if bottom > cur {
			cur = bottom
		}
		if cur < ans {
			ans = cur
		}
		bottom += int64(grid[1][i])
	}
	return ans
}
