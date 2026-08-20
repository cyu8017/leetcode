// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

import "sort"

func maxSubsequence(nums []int, k int) []int {
	type pair struct{ v, i int }
	arr := make([]pair, len(nums))
	for i, v := range nums {
		arr[i] = pair{v, i}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].v > arr[j].v })
	idx := make([]int, k)
	for i := 0; i < k; i++ {
		idx[i] = arr[i].i
	}
	sort.Ints(idx)
	ans := make([]int, k)
	for i, j := range idx {
		ans[i] = nums[j]
	}
	return ans
}
