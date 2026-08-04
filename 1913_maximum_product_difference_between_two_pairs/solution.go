// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

func maxProductDifference(nums []int) int {
	a, b := 0, 0
	c, d := 100000, 100000
	for _, x := range nums {
		if x > a {
			b, a = a, x
		} else if x > b {
			b = x
		}
		if x < c {
			d, c = c, x
		} else if x < d {
			d = x
		}
	}
	return a*b - c*d
}
