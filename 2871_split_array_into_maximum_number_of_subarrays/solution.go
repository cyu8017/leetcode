// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

func maxSubarrays(nums []int) int {
	ans := 0
	cur := -1
	for _, v := range nums {
		if cur == -1 {
			cur = v
		} else {
			cur &= v
		}
		if cur == 0 {
			ans++
			cur = -1
		}
	}
	if ans == 0 {
		return 1
	}
	return ans
}
