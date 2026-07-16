// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

func findPoisonedDuration(timeSeries []int, duration int) int {
	if len(timeSeries) == 0 {
		return 0
	}
	total := duration
	for index := 1; index < len(timeSeries); index++ {
		gap := timeSeries[index] - timeSeries[index-1]
		if gap < duration {
			total += gap
		} else {
			total += duration
		}
	}
	return total
}
