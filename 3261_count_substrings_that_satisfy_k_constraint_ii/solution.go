// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

func countKConstraintSubstrings(s string, k int, queries [][]int) []int64 {
	n := len(s)
	// For each right endpoint, find leftmost L such that s[L..R] satisfies
	leftMost := make([]int, n)
	z, o, L := 0, 0, 0
	for R := 0; R < n; R++ {
		if s[R] == '0' {
			z++
		} else {
			o++
		}
		for z > k && o > k {
			if s[L] == '0' {
				z--
			} else {
				o--
			}
			L++
		}
		leftMost[R] = L
	}
	// prefix of counts of valid substrings ending at i: (i-leftMost[i]+1)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(i-leftMost[i]+1)
	}
	ans := make([]int64, len(queries))
	for qi, q := range queries {
		l, r := q[0], q[1]
		// binary search first idx >= l where leftMost[idx] > l? 
		// valid substrings fully in [l,r]: for each end e in [l,r], count max(l, leftMost[e])..e
		lo, hi := l, r+1
		for lo < hi {
			mid := (lo + hi) / 2
			if leftMost[mid] < l {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		// ends in [l, lo-1]: leftMost[e] < l, contribute e-l+1
		// ends in [lo, r]: contribute e-leftMost[e]+1
		var res int64
		if lo > l {
			// sum_{e=l}^{lo-1} (e-l+1) = sum_{t=1}^{lo-l} t
			m := int64(lo - l)
			res += m * (m + 1) / 2
		}
		if lo <= r {
			res += pref[r+1] - pref[lo]
		}
		ans[qi] = res
	}
	return ans
}
