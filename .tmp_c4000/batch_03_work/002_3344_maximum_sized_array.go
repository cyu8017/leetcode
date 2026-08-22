// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

func maxSizedArray(s int64) int {
	// max n s.t. sum_{i,j,k} (i|j)*k <= s for i,j,k in 0..n-1
	ok := func(n int64) bool {
		var sum int64
		for i := int64(0); i < n; i++ {
			for j := int64(0); j < n; j++ {
				ij := i | j
				// sum_k k = (n-1)*n/2
				sum += ij * (n - 1) * n / 2
				if sum > s {
					return false
				}
			}
		}
		return sum <= s
	}
	lo, hi := int64(1), int64(2000)
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return int(lo)
}
