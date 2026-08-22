// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/

func minPartitionScore(nums []int, k int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i, x := range nums {
		prefix[i+1] = prefix[i] + int64(x)
	}
	value := func(left, right int) int64 {
		sum := prefix[right] - prefix[left]
		return sum * (sum + 1) / 2
	}
	const inf int64 = 1 << 62
	previous := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		previous[i] = inf
	}
	for parts := 1; parts <= k; parts++ {
		current := make([]int64, n+1)
		for i := range current {
			current[i] = inf
		}
		var compute func(int, int, int, int)
		compute = func(lo, hi, optLo, optHi int) {
			if lo > hi {
				return
			}
			mid := (lo + hi) / 2
			bestIndex := -1
			end := optHi
			if mid-1 < end {
				end = mid - 1
			}
			for split := optLo; split <= end; split++ {
				if previous[split] == inf {
					continue
				}
				candidate := previous[split] + value(split, mid)
				if candidate < current[mid] {
					current[mid] = candidate
					bestIndex = split
				}
			}
			if bestIndex == -1 {
				bestIndex = optLo
			}
			compute(lo, mid-1, optLo, bestIndex)
			compute(mid+1, hi, bestIndex, optHi)
		}
		compute(parts, n, parts-1, n-1)
		previous = current
	}
	return previous[n]
}