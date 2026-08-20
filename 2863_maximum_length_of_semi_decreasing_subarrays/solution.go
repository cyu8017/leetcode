// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

func maxSubarrayLength(nums []int) int {
	n := len(nums)
	ans := 0
	st := []int{}
	for i := n - 1; i >= 0; i-- {
		if len(st) == 0 || nums[i] > nums[st[len(st)-1]] {
			st = append(st, i)
		}
	}
	for i := 0; i < n; i++ {
		for len(st) > 0 && nums[i] > nums[st[len(st)-1]] {
			j := st[len(st)-1]
			st = st[:len(st)-1]
			if j-i+1 > ans {
				ans = j - i + 1
			}
		}
	}
	return ans
}
