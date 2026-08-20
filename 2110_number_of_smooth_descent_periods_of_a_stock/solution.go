// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

func getDescentPeriods(prices []int) int64 {
	var ans, cur int64 = 1, 1
	for i := 1; i < len(prices); i++ {
		if prices[i] == prices[i-1]-1 {
			cur++
		} else {
			cur = 1
		}
		ans += cur
	}
	return ans
}
