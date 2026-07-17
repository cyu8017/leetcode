// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

import "math"

func minMoves(nums []int, k int) int {
	adjusted := []int64{}
	for i, v := range nums {
		if v == 1 {
			adjusted = append(adjusted, int64(i-len(adjusted)))
		}
	}
	m := len(adjusted)
	prefix := make([]int64, m+1)
	for i := 0; i < m; i++ {
		prefix[i+1] = prefix[i] + adjusted[i]
	}
	best := int64(math.MaxInt64)
	for left := 0; left+k <= m; left++ {
		right := left + k
		mid := left + k/2
		median := adjusted[mid]
		cost := median*int64(mid-left) - (prefix[mid] - prefix[left])
		cost += (prefix[right] - prefix[mid+1]) - median*int64(right-mid-1)
		if cost < best {
			best = cost
		}
	}
	return int(best)
}
