// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

import "sort"

func minimumDifference(nums []int, k int) int {
	sort.Ints(nums)
	best := nums[k-1] - nums[0]
	for i := 1; i+k-1 < len(nums); i++ {
		d := nums[i+k-1] - nums[i]
		if d < best {
			best = d
		}
	}
	return best
}
