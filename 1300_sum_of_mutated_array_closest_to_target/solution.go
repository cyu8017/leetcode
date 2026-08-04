// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

func findBestValue(arr []int, target int) int {
	lo, hi := 0, 0
	for _, x := range arr {
		if x > hi {
			hi = x
		}
	}
	sumAt := func(v int) int64 {
		var s int64
		for _, x := range arr {
			if x < v {
				s += int64(x)
			} else {
				s += int64(v)
			}
		}
		return s
	}
	for lo < hi {
		mid := lo + (hi-lo)/2
		if sumAt(mid) < int64(target) {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	before, after := sumAt(lo-1), sumAt(lo)
	if int64(target)-before <= after-int64(target) {
		return lo - 1
	}
	return lo
}
