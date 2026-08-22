// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

import (
	"sort"
)

func perfectPairs(nums []int) int64 {
	n := len(nums)
	absNums := make([]int, n)
	for i, v := range nums {
		if v < 0 {
			absNums[i] = -v
		} else {
			absNums[i] = v
		}
	}
	sort.Ints(absNums)
	var ans int64
	j := 0
	for i := 0; i < n; i++ {
		if j < i+1 {
			j = i + 1
		}
		for j < n && absNums[j] <= 2*absNums[i] {
			j++
		}
		ans += int64(j - i - 1)
	}
	return ans
}
