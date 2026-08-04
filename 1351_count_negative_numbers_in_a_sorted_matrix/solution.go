// LeetCode 1351 - Count Negative Numbers in a Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

func countNegatives(grid [][]int) int {
	answer := 0
	for _, row := range grid {
		lo, hi := 0, len(row)
		for lo < hi {
			mid := (lo + hi) / 2
			if row[mid] < 0 {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		answer += len(row) - lo
	}
	return answer
}
