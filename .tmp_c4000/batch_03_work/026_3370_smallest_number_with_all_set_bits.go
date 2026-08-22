// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

func smallestNumber(n int) int {
	x := 1
	for x < n {
		x = x*2 + 1
	}
	return x
}
