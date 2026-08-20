// LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

func longestSubarray(nums []int) int {
	mx := 0
	for _, x := range nums {
		if x > mx {
			mx = x
		}
	}
	ans, cur := 0, 0
	for _, x := range nums {
		if x == mx {
			cur++
			if cur > ans {
				ans = cur
			}
		} else {
			cur = 0
		}
	}
	return ans
}
