// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	ans := [][]int{{rStart, cStart}}
	if rows*cols == 1 {
		return ans
	}
	r, c := rStart, cStart
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	steps := 1
	for len(ans) < rows*cols {
		for d := 0; d < 4; d++ {
			dr, dc := dirs[d][0], dirs[d][1]
			for i := 0; i < steps; i++ {
				r += dr
				c += dc
				if r >= 0 && r < rows && c >= 0 && c < cols {
					ans = append(ans, []int{r, c})
					if len(ans) == rows*cols {
						return ans
					}
				}
			}
			if d%2 == 1 {
				steps++
			}
		}
	}
	return ans
}
