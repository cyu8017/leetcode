// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

func maxRunTime(n int, batteries []int) int64 {
	var sum int64
	for _, b := range batteries {
		sum += int64(b)
	}
	lo, hi := int64(1), sum/int64(n)
	can := func(t int64) bool {
		var need int64
		for _, b := range batteries {
			if int64(b) > t {
				need += t
			} else {
				need += int64(b)
			}
		}
		return need >= t*int64(n)
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
