// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/


func maximizeWin(prizePositions []int, k int) int {
	n := len(prizePositions)
	dp := make([]int, n+1)
	ans := 0
	left := 0
	for right := 0; right < n; right++ {
		for prizePositions[right]-prizePositions[left] > k {
			left++
		}
		cur := right - left + 1
		if dp[left]+cur > ans {
			ans = dp[left] + cur
		}
		best := cur
		if dp[right] > best {
			best = dp[right]
		}
		dp[right+1] = best
	}
	return ans
}
