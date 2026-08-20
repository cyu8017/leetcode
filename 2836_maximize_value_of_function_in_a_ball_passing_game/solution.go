// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

func getMaxFunctionValue(receiver []int, k int64) int64 {
	n := len(receiver)
	const LOG = 36
	up := make([][]int, LOG)
	sum := make([][]int64, LOG)
	for j := 0; j < LOG; j++ {
		up[j] = make([]int, n)
		sum[j] = make([]int64, n)
	}
	for i := 0; i < n; i++ {
		up[0][i] = receiver[i]
		sum[0][i] = int64(receiver[i])
	}
	for j := 1; j < LOG; j++ {
		for i := 0; i < n; i++ {
			mid := up[j-1][i]
			up[j][i] = up[j-1][mid]
			sum[j][i] = sum[j-1][i] + sum[j-1][mid]
		}
	}
	var ans int64
	for i := 0; i < n; i++ {
		cur := i
		total := int64(i)
		kk := k
		for j := 0; j < LOG; j++ {
			if kk&(1<<j) != 0 {
				total += sum[j][cur]
				cur = up[j][cur]
			}
		}
		if total > ans {
			ans = total
		}
	}
	return ans
}
