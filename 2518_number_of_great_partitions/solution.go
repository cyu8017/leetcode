// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

func countPartitions(nums []int, k int) int {
	const MOD = 1000000007
	sum := 0
	for _, x := range nums {
		sum += x
	}
	if sum < 2*k {
		return 0
	}
	dp := make([]int, k)
	dp[0] = 1
	for _, x := range nums {
		for s := k - 1; s >= x; s-- {
			dp[s] = (dp[s] + dp[s-x]) % MOD
		}
	}
	bad := 0
	for _, v := range dp {
		bad = (bad + v) % MOD
	}
	total := 1
	for range nums {
		total = total * 2 % MOD
	}
	ans := (total - 2*bad%MOD + MOD) % MOD
	return ans
}
