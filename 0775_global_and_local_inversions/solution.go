// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

func isIdealPermutation(nums []int) bool {
	for i, v := range nums {
		diff := v - i
		if diff < 0 {
			diff = -diff
		}
		if diff > 1 {
			return false
		}
	}
	return true
}
