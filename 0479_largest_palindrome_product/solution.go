// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

import (
	"math"
	"strconv"
)

func buildPalindrome(value int) int64 {
	text := strconv.Itoa(value)
	reversed := make([]byte, len(text))
	for index := range text {
		reversed[len(text)-1-index] = text[index]
	}
	candidate, _ := strconv.ParseInt(text+string(reversed), 10, 64)
	return candidate
}

func largestPalindrome(n int) int {
	if n == 1 {
		return 9
	}
	upper := int(math.Pow10(n)) - 1
	lower := int(math.Pow10(n - 1))
	for first := upper; first >= lower; first-- {
		candidate := buildPalindrome(first)
		for factor := upper; int64(factor)*int64(factor) >= candidate; factor-- {
			if candidate%int64(factor) == 0 {
				partner := candidate / int64(factor)
				if partner >= int64(lower) && partner <= int64(upper) {
					return int(candidate % 1337)
				}
			}
		}
	}
	return 0
}
