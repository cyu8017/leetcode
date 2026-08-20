// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

import "strconv"

func reorderedPowerOf2(n int) bool {
	countDigits := func(x int) [10]int {
		var c [10]int
		s := strconv.Itoa(x)
		for i := 0; i < len(s); i++ {
			c[s[i]-'0']++
		}
		return c
	}
	target := countDigits(n)
	for i := 0; i < 31; i++ {
		if countDigits(1<<i) == target {
			return true
		}
	}
	return false
}
