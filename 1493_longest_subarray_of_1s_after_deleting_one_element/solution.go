// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

func longestSubarray(nums []int) int {
	left, zeros, ans := 0, 0, 0
	for right, x := range nums {
		if x == 0 {
			zeros++
		}
		for zeros > 1 {
			if nums[left] == 0 {
				zeros--
			}
			left++
		}
		if right-left > ans {
			ans = right - left
		}
	}
	return ans
}
