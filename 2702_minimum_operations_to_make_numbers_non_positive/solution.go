// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/


func minOperations(nums []int, x int, y int) int {
	ok := func(ops int) bool {
		extra := 0
		for _, v := range nums {
			remain := v - ops*y
			if remain > 0 {
				extra += (remain + (x - y) - 1) / (x - y)
			}
		}
		return extra <= ops
	}
	lo, hi := 0, 0
	for _, v := range nums {
		if (v+y-1)/y > hi {
			hi = (v + y - 1) / y
		}
		if (v+x-1)/x > hi {
			hi = (v + x - 1) / x
		}
	}
	hi += len(nums)
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
