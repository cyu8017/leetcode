// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

func findKthNumber(n int, k int) int {
	current := int64(1)
	remaining := int64(k - 1)

	for remaining > 0 {
		steps := countSteps(n, current, current+1)
		if steps <= remaining {
			current++
			remaining -= steps
		} else {
			current *= 10
			remaining--
		}
	}
	return int(current)
}

func countSteps(n int, first, last int64) int64 {
	steps := int64(0)
	for first <= int64(n) {
		upper := last
		if int64(n)+1 < upper {
			upper = int64(n) + 1
		}
		steps += upper - first
		first *= 10
		last *= 10
	}
	return steps
}
