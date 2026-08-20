// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

func minTime(s string, order []int, k int) int {
	n := len(s)
	total := int64(n) * int64(n+1) / 2
	if int64(k) > total {
		return -1
	}
	// Binary search on t
	countValid := func(t int) int64 {
		star := make([]bool, n)
		for i := 0; i <= t; i++ {
			star[order[i]] = true
		}
		// invalid substrings are those entirely in gaps between stars
		var invalid int64
		i := 0
		for i < n {
			if star[i] {
				i++
				continue
			}
			j := i
			for j < n && !star[j] {
				j++
			}
			L := int64(j - i)
			invalid += L * (L + 1) / 2
			i = j
		}
		return total - invalid
	}
	lo, hi, ans := 0, n-1, -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if countValid(mid) >= int64(k) {
			ans = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return ans
}
