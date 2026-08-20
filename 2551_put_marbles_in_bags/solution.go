// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/


import "sort"

func putMarbles(weights []int, k int) int64 {
	n := len(weights)
	if k == 1 || k == n {
		return 0
	}
	pair := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		pair[i] = weights[i] + weights[i+1]
	}
	sort.Ints(pair)
	var mn, mx int64
	for i := 0; i < k-1; i++ {
		mn += int64(pair[i])
		mx += int64(pair[n-2-i])
	}
	return mx - mn
}
