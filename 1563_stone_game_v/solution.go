// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/

func stoneGameV(stoneValue []int) int {
	n := len(stoneValue)
	if n == 0 {
		return 0
	}
	pre := make([]int, n+1)
	for i, x := range stoneValue {
		pre[i+1] = pre[i] + x
	}
	dp := make([][]int, n)
	left := make([][]int, n)
	right := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		left[i] = make([]int, n)
		right[i] = make([]int, n)
		left[i][i] = stoneValue[i]
		right[i][i] = stoneValue[i]
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			lo, hi := i, j-1
			for lo <= hi {
				mid := (lo + hi) / 2
				if 2*(pre[mid+1]-pre[i]) >= pre[j+1]-pre[i] {
					hi = mid - 1
				} else {
					lo = mid + 1
				}
			}
			split := lo
			leftSum := pre[split+1] - pre[i]
			rightSum := pre[j+1] - pre[split+1]
			best := right[split+1][j]
			if leftSum == rightSum {
				if left[i][split] > best {
					best = left[i][split]
				}
			} else if split > i {
				if left[i][split-1] > best {
					best = left[i][split-1]
				}
			}
			dp[i][j] = best
			total := pre[j+1] - pre[i]
			left[i][j] = left[i][j-1]
			if total+best > left[i][j] {
				left[i][j] = total + best
			}
			right[i][j] = right[i+1][j]
			if total+best > right[i][j] {
				right[i][j] = total + best
			}
		}
	}
	return dp[0][n-1]
}
