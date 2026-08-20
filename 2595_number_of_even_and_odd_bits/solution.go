// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/


func evenOddBit(n int) []int {
	even, odd, i := 0, 0, 0
	for n > 0 {
		if n&1 == 1 {
			if i%2 == 0 {
				even++
			} else {
				odd++
			}
		}
		n >>= 1
		i++
	}
	return []int{even, odd}
}
