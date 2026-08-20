// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

import (
	"math"
	"strconv"
)

func nearestPalindromic(n string) string {
	length := len(n)
	number, _ := strconv.ParseInt(n, 10, 64)
	candidates := map[int64]struct{}{
		pow10(length-1) - 1: {},
		pow10(length) + 1:   {},
	}

	prefix, _ := strconv.ParseInt(n[:(length+1)/2], 10, 64)
	for _, half := range []int64{prefix - 1, prefix, prefix + 1} {
		text := strconv.FormatInt(half, 10)
		var palindrome string
		if length%2 == 0 {
			palindrome = text + reverseDigits(text)
		} else {
			palindrome = text + reverseDigits(text[:len(text)-1])
		}
		val, _ := strconv.ParseInt(palindrome, 10, 64)
		candidates[val] = struct{}{}
	}
	delete(candidates, number)

	best := int64(0)
	bestDiff := int64(math.MaxInt64)
	first := true
	for value := range candidates {
		diff := value - number
		if diff < 0 {
			diff = -diff
		}
		if first || diff < bestDiff || (diff == bestDiff && value < best) {
			best = value
			bestDiff = diff
			first = false
		}
	}
	return strconv.FormatInt(best, 10)
}

func pow10(exp int) int64 {
	result := int64(1)
	for i := 0; i < exp; i++ {
		result *= 10
	}
	return result
}

func reverseDigits(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
