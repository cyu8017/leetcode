// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

func threeConsecutiveOdds(arr []int) bool {
	run := 0
	for _, value := range arr {
		if value&1 == 1 {
			run++
			if run == 3 {
				return true
			}
		} else {
			run = 0
		}
	}
	return false
}
