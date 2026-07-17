// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

func minSideSum(value, count int) int {
	if value > count {
		return (value - 1 + value - count) * count / 2
	}
	return value*(value-1)/2 + (count - value + 1)
}

func maxValue(n, index, maxSum int) int {
	lo, hi := 1, maxSum
	for lo < hi {
		mid := (lo + hi + 1) / 2
		total := minSideSum(mid, index) + mid + minSideSum(mid, n-index-1)
		if total <= maxSum {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
