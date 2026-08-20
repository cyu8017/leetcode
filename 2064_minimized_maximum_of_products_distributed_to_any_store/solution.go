// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

func minimizedMaximum(n int, quantities []int) int {
	can := func(x int) bool {
		need := 0
		for _, q := range quantities {
			need += (q + x - 1) / x
			if need > n {
				return false
			}
		}
		return true
	}
	lo, hi := 1, 0
	for _, q := range quantities {
		if q > hi {
			hi = q
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if can(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
