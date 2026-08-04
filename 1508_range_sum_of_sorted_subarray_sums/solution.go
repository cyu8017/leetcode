// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

import "sort"

func rangeSum(nums []int, n int, left int, right int) int {
	values := []int{}
	for i := 0; i < n; i++ {
		total := 0
		for j := i; j < n; j++ {
			total += nums[j]
			values = append(values, total)
		}
	}
	sort.Ints(values)
	ans := 0
	for i := left - 1; i < right; i++ {
		ans = (ans + values[i]) % 1000000007
	}
	return ans
}
