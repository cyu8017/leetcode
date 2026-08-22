// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

func countNonDecreasingArrays(digitSum []int) int {
	const mod = 1000000007
	groups := make([][]int, 51)
	for x := 0; x <= 5000; x++ {
		s := 0
		for y := x; y > 0; y /= 10 {
			s += y % 10
		}
		groups[s] = append(groups[s], x)
	}
	prevVals := groups[digitSum[0]]
	dp := make([]int, len(prevVals))
	for i := range dp {
		dp[i] = 1
	}
	for pos := 1; pos < len(digitSum); pos++ {
		curVals := groups[digitSum[pos]]
		next := make([]int, len(curVals))
		j, prefix := 0, 0
		for i, x := range curVals {
			for j < len(prevVals) && prevVals[j] <= x {
				prefix += dp[j]
				if prefix >= mod {
					prefix -= mod
				}
				j++
			}
			next[i] = prefix
		}
		prevVals, dp = curVals, next
	}
	ans := 0
	for _, x := range dp {
		ans += x
		if ans >= mod {
			ans -= mod
		}
	}
	return ans
}