// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

import (
	"strconv"
)

func countBinaryPalindromes(n int64) int {
	if n == 0 {
		return 1
	}
	ans := 1 // 0
	// count all binary palindromes <= n
	s := strconv.FormatInt(n, 2)
	L := len(s)
	// all palindromes with length < L
	for len_ := 1; len_ < L; len_++ {
		half := (len_ + 1) / 2
		ans += 1 << (half - 1)
	}
	// length == L: build from first half
	half := (L + 1) / 2
	prefix := s[:half]
	// count prefixes from 10..0 to prefix-1
	start := 1 << (half - 1)
	prefVal, _ := strconv.ParseInt(prefix, 2, 64)
	ans += int(prefVal) - start
	// check if palindrome from prefix <= n
	pal := []byte(prefix)
	for i := half - 1 - (L % 2); i >= 0; i-- {
		pal = append(pal, prefix[i])
	}
	pval, _ := strconv.ParseInt(string(pal), 2, 64)
	if pval <= n {
		ans++
	}
	return ans
}
