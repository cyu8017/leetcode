// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

func maxPower(stations []int, r int, k int) int64 {
	n := len(stations)
	diff := make([]int64, n+1)
	for i, v := range stations {
		L := i - r
		if L < 0 {
			L = 0
		}
		R := i + r
		if R >= n {
			R = n - 1
		}
		diff[L] += int64(v)
		diff[R+1] -= int64(v)
	}
	power := make([]int64, n)
	cur := int64(0)
	for i := 0; i < n; i++ {
		cur += diff[i]
		power[i] = cur
	}
	ok := func(x int64) bool {
		extra := make([]int64, n+1)
		have, used := int64(0), int64(0)
		for i := 0; i < n; i++ {
			have += extra[i]
			need := x - (power[i] + have)
			if need > 0 {
				used += need
				if used > int64(k) {
					return false
				}
				have += need
				end := i + 2*r
				if end+1 <= n {
					extra[end+1] -= need
				}
			}
		}
		return true
	}
	lo, hi := int64(0), int64(k)
	for _, p := range power {
		if p > hi {
			hi = p
		}
	}
	hi += int64(k)
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
