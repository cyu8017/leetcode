// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/


func goodSubsetofBinaryMatrix(grid [][]int) []int {
	n := len(grid[0])
	first := map[int]int{}
	for i, row := range grid {
		mask := 0
		for j, v := range row {
			if v == 1 {
				mask |= 1 << j
			}
		}
		if mask == 0 {
			return []int{i}
		}
		for m, idx := range first {
			if m&mask == 0 {
				if idx < i {
					return []int{idx, i}
				}
				return []int{i, idx}
			}
		}
		if _, ok := first[mask]; !ok {
			first[mask] = i
		}
	}
	_ = n
	return []int{}
}
