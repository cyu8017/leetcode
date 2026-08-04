// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

func maxProduct(nums []int) int {
	a, b := 0, 0
	for _, v := range nums {
		if v > a {
			b = a
			a = v
		} else if v > b {
			b = v
		}
	}
	return (a - 1) * (b - 1)
}
