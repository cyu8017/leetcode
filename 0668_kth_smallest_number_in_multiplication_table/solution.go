// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

func findKthNumber(m int, n int, k int) int {
	countLe := func(x int) int {
		total := 0
		for row := 1; row <= m; row++ {
			v := x / row
			if v > n {
				v = n
			}
			total += v
		}
		return total
	}
	lo, hi := 1, m*n
	for lo < hi {
		mid := (lo + hi) / 2
		if countLe(mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
