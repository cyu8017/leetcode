// LeetCode 2659 - Make Array Empty
// https://leetcode.com/problems/make-array-empty/


import "sort"

func countOperationsToEmptyArray(nums []int) int64 {
	n := len(nums)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return nums[idx[i]] < nums[idx[j]] })
	ans := int64(n)
	for i := 1; i < n; i++ {
		if idx[i] < idx[i-1] {
			ans += int64(n - i)
		}
	}
	return ans
}
