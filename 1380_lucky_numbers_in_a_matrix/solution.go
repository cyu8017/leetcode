// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

func luckyNumbers(matrix [][]int) []int {
	mins := map[int]bool{}
	for _, row := range matrix {
		mn := row[0]
		for _, v := range row[1:] {
			if v < mn {
				mn = v
			}
		}
		mins[mn] = true
	}
	maxs := map[int]bool{}
	for c := 0; c < len(matrix[0]); c++ {
		mx := matrix[0][c]
		for r := 1; r < len(matrix); r++ {
			if matrix[r][c] > mx {
				mx = matrix[r][c]
			}
		}
		maxs[mx] = true
	}
	var answer []int
	for v := range mins {
		if maxs[v] {
			answer = append(answer, v)
		}
	}
	return answer
}
