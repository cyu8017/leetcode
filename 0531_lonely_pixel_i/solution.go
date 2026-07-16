// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

func findLonelyPixel(picture [][]byte) int {
	rows := len(picture)
	cols := len(picture[0])
	rowCounts := make([]int, rows)
	colCounts := make([]int, cols)

	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if picture[r][c] == 'B' {
				rowCounts[r]++
				colCounts[c]++
			}
		}
	}

	lonely := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if picture[r][c] == 'B' && rowCounts[r] == 1 && colCounts[c] == 1 {
				lonely++
			}
		}
	}
	return lonely
}
