// LeetCode 1344 - Angle Between Hands of a Clock
// https://leetcode.com/problems/angle-between-hands-of-a-clock/

func angleClock(hour int, minutes int) float64 {
	diff := float64((hour%12)*30) + float64(minutes)*0.5 - float64(minutes)*6
	if diff < 0 {
		diff = -diff
	}
	if diff > 360-diff {
		return 360 - diff
	}
	return diff
}
