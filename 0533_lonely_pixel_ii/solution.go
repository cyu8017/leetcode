// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

func findBlackPixel(picture [][]byte, target int) int {
	rows := len(picture)
	cols := len(picture[0])
	rowStrings := make([]string, rows)
	rowCounts := make([]int, rows)
	colCounts := make([]int, cols)

	for r := 0; r < rows; r++ {
		rowStrings[r] = string(picture[r])
		for c := 0; c < cols; c++ {
			if picture[r][c] == 'B' {
				rowCounts[r]++
				colCounts[c]++
			}
		}
	}

	lonely := 0
	for r := 0; r < rows; r++ {
		if rowCounts[r] != target {
			continue
		}
		for c := 0; c < cols; c++ {
			if picture[r][c] != 'B' || colCounts[c] != target {
				continue
			}
			matches := true
			for i := 0; i < rows; i++ {
				if picture[i][c] == 'B' && rowStrings[r] != rowStrings[i] {
					matches = false
					break
				}
			}
			if matches {
				lonely++
			}
		}
	}
	return lonely
}
