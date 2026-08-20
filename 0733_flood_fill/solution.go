// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	original := image[sr][sc]
	if original == color {
		return image
	}
	m, n := len(image), len(image[0])
	var dfs func(r, c int)
	dfs = func(r, c int) {
		if r < 0 || r >= m || c < 0 || c >= n || image[r][c] != original {
			return
		}
		image[r][c] = color
		dfs(r+1, c)
		dfs(r-1, c)
		dfs(r, c+1)
		dfs(r, c-1)
	}
	dfs(sr, sc)
	return image
}
