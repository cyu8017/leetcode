// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

import (
	"sort"
	"strconv"
)

func atMostNGivenDigitSet(digits []string, n int) int {
	sort.Strings(digits)
	s := strconv.Itoa(n)
	m := len(s)
	k := len(digits)

	countLen := func(length int) int {
		res := 1
		for i := 0; i < length; i++ {
			res *= k
		}
		return res
	}

	var countUpTo func(t string) int
	countUpTo = func(t string) int {
		if len(t) == 0 {
			return 0
		}
		first := 0
		for _, d := range digits {
			if d < string(t[0]) {
				first++
			}
		}
		ways := first
		for i := 0; i < len(t)-1; i++ {
			ways *= k
		}
		for _, d := range digits {
			if d == string(t[0]) {
				ways += countUpTo(t[1:])
				break
			}
		}
		return ways
	}

	ans := 0
	for i := 1; i < m; i++ {
		ans += countLen(i)
	}
	ans += countUpTo(s)
	return ans
}
