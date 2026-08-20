// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

import "sort"

func orderlyQueue(s string, k int) string {
	if k > 1 {
		b := []byte(s)
		sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
		return string(b)
	}
	best := s
	for i := 1; i < len(s); i++ {
		cand := s[i:] + s[:i]
		if cand < best {
			best = cand
		}
	}
	return best
}
