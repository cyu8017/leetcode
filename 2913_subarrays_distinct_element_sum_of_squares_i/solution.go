// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

func sumCounts(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		seen := map[int]bool{}
		for j := i; j < n; j++ {
			seen[nums[j]] = true
			d := len(seen)
			ans += d * d
		}
	}
	return ans
}
