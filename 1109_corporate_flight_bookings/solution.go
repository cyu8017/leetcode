// LeetCode 1109 - Corporate Flight Bookings
// https://leetcode.com/problems/corporate-flight-bookings/

func corpFlightBookings(bookings [][]int, n int) []int {
	diff := make([]int, n+1)
	for _, b := range bookings {
		diff[b[0]-1] += b[2]
		diff[b[1]] -= b[2]
	}
	ans := make([]int, n)
	cur := 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		ans[i] = cur
	}
	return ans
}
