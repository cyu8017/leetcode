// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

func findRotation(mat [][]int, target [][]int) bool {
	current := mat
	for rotation := 0; rotation < 4; rotation++ {
		if matricesEqual(current, target) {
			return true
		}
		n := len(current)
		rotated := make([][]int, n)
		for i := range rotated {
			rotated[i] = make([]int, n)
		}
		for col := 0; col < n; col++ {
			for row := 0; row < n; row++ {
				rotated[col][row] = current[n-1-row][col]
			}
		}
		current = rotated
	}
	return false
}

func matricesEqual(a, b [][]int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if len(a[i]) != len(b[i]) {
			return false
		}
		for j := range a[i] {
			if a[i][j] != b[i][j] {
				return false
			}
		}
	}
	return true
}
