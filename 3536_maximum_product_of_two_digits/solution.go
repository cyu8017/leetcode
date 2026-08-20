// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

func maxProduct(n int) int {
	a, b := 0, 0
	for ; n > 0; n /= 10 {
		x := n % 10
		if a < x {
			b, a = a, x
		} else if b < x {
			b = x
		}
	}
	return a * b
}
