// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/


func buyChoco(prices []int, money int) int {
	a, b := int(1e9), int(1e9)
	for _, p := range prices {
		if p < a {
			b = a
			a = p
		} else if p < b {
			b = p
		}
	}
	if a+b <= money {
		return money - a - b
	}
	return money
}
