// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

import "strconv"

func countSymmetricIntegers(low int, high int) int {
	ans := 0
	for x := low; x <= high; x++ {
		s := strconv.Itoa(x)
		if len(s)%2 != 0 {
			continue
		}
		mid := len(s) / 2
		a, b := 0, 0
		for i := 0; i < mid; i++ {
			a += int(s[i] - '0')
			b += int(s[mid+i] - '0')
		}
		if a == b {
			ans++
		}
	}
	return ans
}
