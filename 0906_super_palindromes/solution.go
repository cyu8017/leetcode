// LeetCode 0906 - Super Palindromes
// https://leetcode.com/problems/super-palindromes/

import "strconv"

func superpalindromesInRange(left string, right string) int {
	L, _ := strconv.ParseInt(left, 10, 64)
	R, _ := strconv.ParseInt(right, 10, 64)

	isPal := func(x int64) bool {
		s := strconv.FormatInt(x, 10)
		for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
			if s[i] != s[j] {
				return false
			}
		}
		return true
	}

	ans := 0
	for k := 1; k <= 100000; k++ {
		s := strconv.Itoa(k)
		rev := reverseStr(s)
		pal, _ := strconv.ParseInt(s+rev, 10, 64)
		sq := pal * pal
		if sq > R {
			break
		}
		if sq >= L && isPal(sq) {
			ans++
		}
	}
	for k := 1; k <= 100000; k++ {
		s := strconv.Itoa(k)
		rev := reverseStr(s[:len(s)-1])
		pal, _ := strconv.ParseInt(s+rev, 10, 64)
		sq := pal * pal
		if sq > R {
			break
		}
		if sq >= L && isPal(sq) {
			ans++
		}
	}
	return ans
}

func reverseStr(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
