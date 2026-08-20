// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

func minimumOperations(nums []int) int {
	n := len(nums)
	dp := make([][4]int, n+1)
	for i := 0; i <= n; i++ {
		for g := 1; g <= 3; g++ {
			dp[i][g] = 1 << 30
		}
	}
	dp[0][1], dp[0][2], dp[0][3] = 0, 0, 0
	for i := 1; i <= n; i++ {
		v := nums[i-1]
		for g := 1; g <= 3; g++ {
			cost := 0
			if v != g {
				cost = 1
			}
			for prev := 1; prev <= g; prev++ {
				cand := dp[i-1][prev] + cost
				if cand < dp[i][g] {
					dp[i][g] = cand
				}
			}
		}
	}
	ans := dp[n][1]
	if dp[n][2] < ans {
		ans = dp[n][2]
	}
	if dp[n][3] < ans {
		ans = dp[n][3]
	}
	return ans
}
