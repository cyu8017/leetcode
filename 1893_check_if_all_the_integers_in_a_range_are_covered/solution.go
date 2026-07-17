// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

func isCovered(ranges [][]int, left int, right int) bool {
	covered := make([]bool, 51)
	for _, interval := range ranges {
		for value := interval[0]; value <= interval[1]; value++ {
			covered[value] = true
		}
	}
	for value := left; value <= right; value++ {
		if !covered[value] {
			return false
		}
	}
	return true
}
