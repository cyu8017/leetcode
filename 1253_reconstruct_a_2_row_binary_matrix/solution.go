// LeetCode 1253 - Reconstruct a 2-Row Binary Matrix
// https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

func reconstructMatrix(upper int, lower int, colsum []int) [][]int {
	top := make([]int, len(colsum))
	bottom := make([]int, len(colsum))
	for i, value := range colsum {
		if value == 2 {
			top[i], bottom[i] = 1, 1
			upper--
			lower--
		}
	}
	if upper < 0 || lower < 0 {
		return [][]int{}
	}
	for i, value := range colsum {
		if value == 1 {
			if upper > 0 {
				top[i] = 1
				upper--
			} else if lower > 0 {
				bottom[i] = 1
				lower--
			} else {
				return [][]int{}
			}
		}
	}
	if upper == 0 && lower == 0 {
		return [][]int{top, bottom}
	}
	return [][]int{}
}
