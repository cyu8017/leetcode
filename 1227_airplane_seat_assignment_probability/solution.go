// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

func nthPersonGetsNthSeat(n int) float64 {
	if n == 1 {
		return 1.0
	}
	return 0.5
}
