// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

func kLengthApart(nums []int, k int) bool {
	previous := -k - 1
	for i, value := range nums {
		if value == 1 {
			if i-previous <= k {
				return false
			}
			previous = i
		}
	}
	return true
}
