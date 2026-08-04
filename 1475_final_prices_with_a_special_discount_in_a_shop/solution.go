// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

func finalPrices(prices []int) []int {
	ans := append([]int(nil), prices...)
	stack := []int{}
	for i, price := range prices {
		for len(stack) > 0 && prices[stack[len(stack)-1]] >= price {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[j] -= price
		}
		stack = append(stack, i)
	}
	return ans
}
