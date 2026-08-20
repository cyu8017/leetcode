// LeetCode 3733 - Minimum Time to Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

func minimumTime(d []int, r []int) int64 {
	ok := func(T int64) bool {
		w0 := T - T/int64(r[0])
		w1 := T - T/int64(r[1])
		return w0+w1 >= int64(d[0])+int64(d[1])
	}
	lo, hi := int64(1), int64(8e18)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
