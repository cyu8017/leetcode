// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

func smallestNumber(n int, t int) int {
	for x := n; ; x++ {
		p, y := 1, x
		for y > 0 {
			p *= y % 10
			y /= 10
		}
		if p%t == 0 {
			return x
		}
	}
}
