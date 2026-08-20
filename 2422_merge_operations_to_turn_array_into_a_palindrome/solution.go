// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

func minimumOperations(nums []int) int {
	l, r := 0, len(nums)-1
	left, right := nums[l], nums[r]
	ans := 0
	for l < r {
		if left == right {
			l++
			r--
			if l < r {
				left, right = nums[l], nums[r]
			}
		} else if left < right {
			l++
			left += nums[l]
			ans++
		} else {
			r--
			right += nums[r]
			ans++
		}
	}
	return ans
}
