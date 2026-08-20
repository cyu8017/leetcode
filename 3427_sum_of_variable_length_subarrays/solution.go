// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

func subarraySum(nums []int) int {
	n := len(nums)
	pref := make([]int, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + x
	}
	ans := 0
	for i := 0; i < n; i++ {
		start := i - nums[i]
		if start < 0 {
			start = 0
		}
		ans += pref[i+1] - pref[start]
	}
	return ans
}
