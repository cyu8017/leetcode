// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/


import "sort"
func minimumTime(hens []int, grains []int) int {
	sort.Ints(hens)
	sort.Ints(grains)
	ok := func(t int) bool {
		j := 0
		for _, h := range hens {
			if j >= len(grains) {
				return true
			}
			if grains[j] >= h {
				// only go right
				for j < len(grains) && grains[j]-h <= t {
					j++
				}
			} else {
				if h-grains[j] > t {
					return false
				}
				left := h - grains[j]
				// option1: left then right
				maxRight1 := t - 2*left
				// option2: right then left
				maxRight2 := (t - left) / 2
				reach := h
				if maxRight1 > maxRight2 {
					if maxRight1 > 0 {
						reach = h + maxRight1
					}
				} else {
					if maxRight2 > 0 {
						reach = h + maxRight2
					}
				}
				for j < len(grains) && grains[j] <= reach {
					j++
				}
			}
		}
		return j >= len(grains)
	}
	lo, hi := 0, int(2e9)
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
