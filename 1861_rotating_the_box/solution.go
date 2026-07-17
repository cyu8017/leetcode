// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

func rotateTheBox(boxGrid [][]byte) [][]byte {
	m, n := len(boxGrid), len(boxGrid[0])
	rotated := make([][]byte, n)
	for i := range rotated {
		rotated[i] = make([]byte, m)
		for j := range rotated[i] {
			rotated[i][j] = '.'
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			rotated[i][j] = boxGrid[m-1-j][i]
		}
	}

	for col := 0; col < m; col++ {
		row := n - 1
		for i := n - 1; i >= 0; i-- {
			if rotated[i][col] == '*' {
				row = i - 1
			} else if rotated[i][col] == '#' {
				rotated[i][col] = '.'
				rotated[row][col] = '#'
				row--
			}
		}
	}

	return rotated
}
