// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

func shipWithinDays(weights []int, days int) int {
	lo, hi := 0, 0
	for _, w := range weights {
		if w > lo {
			lo = w
		}
		hi += w
	}
	can := func(cap int) bool {
		need, cur := 1, 0
		for _, w := range weights {
			if cur+w > cap {
				need++
				cur = 0
			}
			cur += w
		}
		return need <= days
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
