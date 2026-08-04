// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

func containsPattern(arr []int, m int, k int) bool {
	run := 0
	for i := m; i < len(arr); i++ {
		if arr[i] == arr[i-m] {
			run++
		} else {
			run = 0
		}
		if run >= m*(k-1) {
			return true
		}
	}
	return false
}
