// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

import "sort"

func answerQueries(nums []int, queries []int) []int {
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		ans[i] = sort.Search(len(nums), func(j int) bool { return nums[j] > q })
	}
	return ans
}
