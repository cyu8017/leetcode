// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

func longestNiceSubarray(nums []int) int {
	used, left, ans := 0, 0, 0
	for right, x := range nums {
		for used&x != 0 {
			used ^= nums[left]
			left++
		}
		used |= x
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}
	return ans
}
