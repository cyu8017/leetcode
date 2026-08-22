// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

func minLength(s string, numOps int) int {
	n := len(s)
	ok := func(L int) bool {
		ops := 0
		i := 0
		for i < n {
			j := i
			for j < n && s[j] == s[i] {
				j++
			}
			ops += (j - i) / (L + 1)
			i = j
		}
		return ops <= numOps
	}
	lo, hi := 1, n
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
