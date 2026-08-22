// LeetCode 3801 - Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

func minMergeCost(lists [][]int) int64 {
	m := len(lists)
	totalMasks := 1 << m
	merged := make([][]int, totalMasks)
	length, median := make([]int, totalMasks), make([]int, totalMasks)
	for mask := 1; mask < totalMasks; mask++ {
		bit := mask & -mask
		index := 0
		for 1<<index != bit {
			index++
		}
		previous := merged[mask^bit]
		current := lists[index]
		out := make([]int, 0, len(previous)+len(current))
		i, j := 0, 0
		for i < len(previous) || j < len(current) {
			if j == len(current) || (i < len(previous) && previous[i] <= current[j]) {
				out = append(out, previous[i])
				i++
			} else {
				out = append(out, current[j])
				j++
			}
		}
		merged[mask] = out
		length[mask] = len(out)
		median[mask] = out[(len(out)-1)/2]
	}
	const inf int64 = 1 << 62
	dp := make([]int64, totalMasks)
	for mask := 1; mask < totalMasks; mask++ {
		if mask&(mask-1) == 0 {
			continue
		}
		dp[mask] = inf
		firstBit := mask & -mask
		for left := (mask - 1) & mask; left > 0; left = (left - 1) & mask {
			if left&firstBit == 0 {
				continue
			}
			right := mask ^ left
			if right == 0 {
				continue
			}
			diff := median[left] - median[right]
			if diff < 0 {
				diff = -diff
			}
			candidate := dp[left] + dp[right] + int64(length[mask]+diff)
			if candidate < dp[mask] {
				dp[mask] = candidate
			}
		}
	}
	return dp[totalMasks-1]
}