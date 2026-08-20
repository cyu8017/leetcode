// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

func countPrimeSetBits(left int, right int) int {
	primes := map[int]bool{2: true, 3: true, 5: true, 7: true, 11: true, 13: true, 17: true, 19: true}
	ans := 0
	for num := left; num <= right; num++ {
		bits := 0
		x := num
		for x > 0 {
			bits += x & 1
			x >>= 1
		}
		if primes[bits] {
			ans++
		}
	}
	return ans
}
