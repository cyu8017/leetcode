// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

func lexSmallest(s string) string {
	n := len(s)
	best := s
	b := []byte(s)
	for i := 1; i <= n; i++ {
		t := append([]byte{}, b...)
		for l, r := 0, i-1; l < r; l, r = l+1, r-1 {
			t[l], t[r] = t[r], t[l]
		}
		if string(t) < best {
			best = string(t)
		}
	}
	for i := 0; i < n; i++ {
		t := append([]byte{}, b...)
		for l, r := i, n-1; l < r; l, r = l+1, r-1 {
			t[l], t[r] = t[r], t[l]
		}
		if string(t) < best {
			best = string(t)
		}
	}
	return best
}
