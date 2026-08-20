// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

func minimumFinishTime(tires [][]int, changeTime int, numLaps int) int {
	minTime := make([]int, 20)
	for i := range minTime {
		minTime[i] = 1 << 30
	}
	for _, tire := range tires {
		f, r := tire[0], tire[1]
		t, lap := f, f
		for x := 1; x < 20 && t < minTime[x]; x++ {
			minTime[x] = t
			lap *= r
			if lap > changeTime+f {
				break
			}
			t += lap
		}
	}
	dp := make([]int, numLaps+1)
	for i := range dp {
		dp[i] = 1 << 30
	}
	dp[0] = -changeTime
	for i := 1; i <= numLaps; i++ {
		for j := 1; j <= i && j < 20; j++ {
			cand := dp[i-j] + changeTime + minTime[j]
			if cand < dp[i] {
				dp[i] = cand
			}
		}
	}
	return dp[numLaps]
}
