// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

import "sort"

func lexicographicallySmallestArray(nums []int, limit int) []int {
	n := len(nums)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return nums[idx[i]] < nums[idx[j]] })
	ans := make([]int, n)
	for i := 0; i < n; {
		j := i + 1
		for j < n && nums[idx[j]]-nums[idx[j-1]] <= limit {
			j++
		}
		groupIdx := append([]int{}, idx[i:j]...)
		sort.Ints(groupIdx)
		vals := make([]int, j-i)
		for t := i; t < j; t++ {
			vals[t-i] = nums[idx[t]]
		}
		for t, gi := range groupIdx {
			ans[gi] = vals[t]
		}
		i = j
	}
	return ans
}
