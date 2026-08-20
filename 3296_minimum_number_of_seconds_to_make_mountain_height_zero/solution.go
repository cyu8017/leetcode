// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

func minNumberOfSeconds(mountainHeight int, workerTimes []int) int64 {
	ok := func(t int64) bool {
		var total int64
		for _, w := range workerTimes {
			// max x s.t. w*(1+..+x)=w*x*(x+1)/2 <= t
			lo, hi := int64(0), int64(mountainHeight)
			for lo < hi {
				mid := (lo + hi + 1) / 2
				if int64(w)*mid*(mid+1)/2 <= t {
					lo = mid
				} else {
					hi = mid - 1
				}
			}
			total += lo
			if total >= int64(mountainHeight) {
				return true
			}
		}
		return total >= int64(mountainHeight)
	}
	lo, hi := int64(0), int64(1e18)
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
