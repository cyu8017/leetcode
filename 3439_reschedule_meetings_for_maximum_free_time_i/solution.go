// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
	n := len(startTime)
	gaps := make([]int, n+1)
	gaps[0] = startTime[0]
	for i := 1; i < n; i++ {
		gaps[i] = startTime[i] - endTime[i-1]
	}
	gaps[n] = eventTime - endTime[n-1]
	// merge k+1 consecutive gaps by moving k meetings
	window := k + 1
	sum := 0
	for i := 0; i < window && i < len(gaps); i++ {
		sum += gaps[i]
	}
	ans := sum
	for i := window; i < len(gaps); i++ {
		sum += gaps[i] - gaps[i-window]
		if sum > ans {
			ans = sum
		}
	}
	return ans
}
