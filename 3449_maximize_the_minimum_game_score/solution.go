// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

func maxScore(points []int, m int) int64 {
	ok := func(mid int64) bool {
		var need int64
		extra := int64(0)
		for _, p := range points {
			req := (mid + int64(p) - 1) / int64(p)
			if req > extra {
				visits := req - extra
				need += 2*visits - 1
				extra = visits - 1
			} else {
				need += 1
				extra = 0
			}
			if need > int64(m) {
				return false
			}
		}
		return need <= int64(m)
	}
	lo, hi := int64(0), int64(1e18)
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
