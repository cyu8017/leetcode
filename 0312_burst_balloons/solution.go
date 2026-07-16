// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

func maxCoins(nums []int) int {
	balloons := make([]int, 0, len(nums)+2)
	balloons = append(balloons, 1)
	balloons = append(balloons, nums...)
	balloons = append(balloons, 1)

	size := len(balloons)
	dp := make([][]int, size)
	for index := 0; index < size; index++ {
		dp[index] = make([]int, size)
	}

	for length := 3; length <= size; length++ {
		for left := 0; left <= size-length; left++ {
			right := left + length - 1
			for mid := left + 1; mid < right; mid++ {
				coins := dp[left][mid] + dp[mid][right] + balloons[left]*balloons[mid]*balloons[right]
				if coins > dp[left][right] {
					dp[left][right] = coins
				}
			}
		}
	}

	return dp[0][size-1]
}
