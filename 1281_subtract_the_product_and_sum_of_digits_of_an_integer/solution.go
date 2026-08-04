// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

func subtractProductAndSum(n int) int {
	product, total := 1, 0
	for n > 0 {
		digit := n % 10
		n /= 10
		product *= digit
		total += digit
	}
	return product - total
}
