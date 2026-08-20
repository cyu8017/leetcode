// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

import "strconv"

func primePalindrome(n int) int {
	isPrime := func(x int) bool {
		if x < 2 {
			return false
		}
		if x%2 == 0 {
			return x == 2
		}
		for d := 3; d*d <= x; d += 2 {
			if x%d == 0 {
				return false
			}
		}
		return true
	}
	pals := func() int {
		for length := 1; length <= 5; length++ {
			start := 1
			for i := 1; i < length; i++ {
				start *= 10
			}
			end := start * 10
			for root := start; root < end; root++ {
				s := strconv.Itoa(root)
				rev := []byte(s)
				for i, j := 0, len(rev)-1; i < j; i, j = i+1, j-1 {
					rev[i], rev[j] = rev[j], rev[i]
				}
				palStr := s + string(rev[1:])
				pal, _ := strconv.Atoi(palStr)
				if pal >= n && isPrime(pal) {
					return pal
				}
			}
		}
		return 0
	}
	if n <= 2 {
		return 2
	}
	if n <= 3 {
		return 3
	}
	if n <= 5 {
		return 5
	}
	if n <= 7 {
		return 7
	}
	if n <= 11 {
		return 11
	}
	return pals()
}
