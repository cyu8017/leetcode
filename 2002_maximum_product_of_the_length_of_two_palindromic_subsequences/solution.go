// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

func maxProduct(s string) int {
	n := len(s)
	isPal := func(mask int) (bool, int) {
		chars := []byte{}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				chars = append(chars, s[i])
			}
		}
		for l, r := 0, len(chars)-1; l < r; l, r = l+1, r-1 {
			if chars[l] != chars[r] {
				return false, 0
			}
		}
		return true, len(chars)
	}
	best := 0
	total := 1 << n
	for mask1 := 1; mask1 < total; mask1++ {
		ok1, len1 := isPal(mask1)
		if !ok1 {
			continue
		}
		remain := (total - 1) ^ mask1
		for mask2 := remain; mask2 > 0; mask2 = (mask2 - 1) & remain {
			ok2, len2 := isPal(mask2)
			if ok2 && len1*len2 > best {
				best = len1 * len2
			}
		}
	}
	return best
}
