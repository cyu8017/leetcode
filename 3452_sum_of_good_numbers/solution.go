// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

func sumOfGoodNumbers(nums []int, k int) int {
	ans := 0
	n := len(nums)
	for i, x := range nums {
		good := true
		if i-k >= 0 && x <= nums[i-k] {
			good = false
		}
		if i+k < n && x <= nums[i+k] {
			good = false
		}
		if good {
			ans += x
		}
	}
	return ans
}
