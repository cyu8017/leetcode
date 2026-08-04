// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

func minSpaceWastedKResizing(nums []int, k int) int {
	n := len(nums)
	const INF = int(1e18)
	waste := make([][]int, n)
	for i := 0; i < n; i++ {
		waste[i] = make([]int, n)
		mx, total := 0, 0
		for j := i; j < n; j++ {
			if nums[j] > mx {
				mx = nums[j]
			}
			total += nums[j]
			waste[i][j] = mx*(j-i+1) - total
		}
	}
	segments := k + 1
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, segments+1)
		for s := range dp[i] {
			dp[i][s] = INF
		}
	}
	dp[0][0] = 0
	for i := 1; i <= n; i++ {
		limit := segments
		if i < limit {
			limit = i
		}
		for s := 1; s <= limit; s++ {
			for p := s - 1; p < i; p++ {
				v := dp[p][s-1] + waste[p][i-1]
				if v < dp[i][s] {
					dp[i][s] = v
				}
			}
		}
	}
	best := INF
	for s := 1; s <= segments; s++ {
		if dp[n][s] < best {
			best = dp[n][s]
		}
	}
	return best
}
