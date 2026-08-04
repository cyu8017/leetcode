// LeetCode 1262 - Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/

func maxSumDivThree(nums []int) int {
	const impossible = -1 << 60
	dp := [3]int{0, impossible, impossible}
	for _, value := range nums {
		old := dp
		for _, total := range old {
			if total == impossible {
				continue
			}
			rem := (total + value) % 3
			if total+value > dp[rem] {
				dp[rem] = total + value
			}
		}
	}
	return dp[0]
}
