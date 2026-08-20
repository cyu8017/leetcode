// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/


import "sort"

func countTheNumOfKFreeSubsets(nums []int, k int) int64 {
	sort.Ints(nums)
	groups := map[int][]int{}
	for _, x := range nums {
		groups[x%k] = append(groups[x%k], x)
	}
	ans := int64(1)
	for _, g := range groups {
		// chain by +k
		prevVal := -1
		prevTake, prevSkip := int64(0), int64(1)
		for _, v := range g {
			take, skip := int64(0), prevTake+prevSkip
			if prevVal+k == v {
				take = prevSkip
			} else {
				take = prevTake + prevSkip
			}
			prevTake, prevSkip = take, skip
			prevVal = v
		}
		ans *= prevTake + prevSkip
	}
	return ans
}
