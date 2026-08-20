// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

import "strconv"

func rotatedDigits(n int) int {
	valid := map[byte]bool{'0': true, '1': true, '2': true, '5': true, '6': true, '8': true, '9': true}
	changing := map[byte]bool{'2': true, '5': true, '6': true, '9': true}
	count := 0
	for num := 1; num <= n; num++ {
		s := strconv.Itoa(num)
		ok, changed := true, false
		for i := 0; i < len(s); i++ {
			if !valid[s[i]] {
				ok = false
				break
			}
			if changing[s[i]] {
				changed = true
			}
		}
		if ok && changed {
			count++
		}
	}
	return count
}
