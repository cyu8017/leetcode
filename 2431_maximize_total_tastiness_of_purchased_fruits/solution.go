// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

func maxTastiness(price []int, tastiness []int, maxAmount int, maxCoupons int) int {
	n := len(price)
	dp := make([][]int, maxAmount+1)
	for i := range dp {
		dp[i] = make([]int, maxCoupons+1)
		for j := range dp[i] {
			dp[i][j] = -1 << 30
		}
	}
	dp[0][0] = 0
	for i := 0; i < n; i++ {
		p, t := price[i], tastiness[i]
		for a := maxAmount; a >= 0; a-- {
			for c := maxCoupons; c >= 0; c-- {
				if dp[a][c] < 0 {
					continue
				}
				if a+p <= maxAmount {
					if dp[a][c]+t > dp[a+p][c] {
						dp[a+p][c] = dp[a][c] + t
					}
				}
				if c+1 <= maxCoupons && a+p/2 <= maxAmount {
					if dp[a][c]+t > dp[a+p/2][c+1] {
						dp[a+p/2][c+1] = dp[a][c] + t
					}
				}
			}
		}
	}
	ans := 0
	for a := 0; a <= maxAmount; a++ {
		for c := 0; c <= maxCoupons; c++ {
			if dp[a][c] > ans {
				ans = dp[a][c]
			}
		}
	}
	return ans
}
