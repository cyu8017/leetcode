// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

func minTotalTime(forward []int, backward []int, queries []int) int64 {
	n := len(forward)
	sumB := 0
	for _, v := range backward {
		sumB += v
	}
	pf := make([]int, n+1)
	for i := 0; i < n; i++ {
		pf[i+1] = pf[i] + forward[i]
	}
	pb := make([]int, n+1)
	for i := 0; i < n; i++ {
		pb[i+1] = pb[i] + backward[i]
	}
	var ans int64
	pos := 0
	for _, q := range queries {
		r := 0
		if q < pos {
			r = pf[n]
		}
		r += pf[q] - pf[pos]
		l := 0
		if q > pos {
			l = sumB
		}
		l += pb[pos] - pb[q]
		if l < r {
			ans += int64(l)
		} else {
			ans += int64(r)
		}
		pos = q
	}
	return ans
}
