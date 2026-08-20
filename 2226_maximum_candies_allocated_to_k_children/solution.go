// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

func maximumCandies(candies []int, k int64) int {
	mx := 0
	for _, c := range candies {
		if c > mx {
			mx = c
		}
	}
	lo, hi := 0, mx
	can := func(mid int) bool {
		if mid == 0 {
			return true
		}
		var cnt int64
		for _, c := range candies {
			cnt += int64(c / mid)
			if cnt >= k {
				return true
			}
		}
		return false
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if can(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
