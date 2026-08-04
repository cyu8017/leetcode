// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

func countOrders(n int) int {
	const mod = 1000000007
	ans := 1
	for i := 1; i <= n; i++ {
		ans = ans * i % mod
		ans = ans * (2*i - 1) % mod
	}
	return ans
}
