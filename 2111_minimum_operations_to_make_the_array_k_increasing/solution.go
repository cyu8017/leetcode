// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

import "sort"

func kIncreasing(arr []int, k int) int {
	ans := 0
	n := len(arr)
	for start := 0; start < k; start++ {
		seq := []int{}
		for i := start; i < n; i += k {
			seq = append(seq, arr[i])
		}
		// LIS length (non-decreasing)
		tails := []int{}
		for _, x := range seq {
			i := sort.SearchInts(tails, x+1)
			if i == len(tails) {
				tails = append(tails, x)
			} else {
				tails[i] = x
			}
		}
		ans += len(seq) - len(tails)
	}
	return ans
}
