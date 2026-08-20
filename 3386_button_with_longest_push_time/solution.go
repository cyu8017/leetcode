// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

func buttonWithLongestTime(events [][]int) int {
	bestT, bestI := events[0][1], events[0][0]
	for i := 1; i < len(events); i++ {
		t := events[i][1] - events[i-1][1]
		if t > bestT || (t == bestT && events[i][0] < bestI) {
			bestT = t
			bestI = events[i][0]
		}
	}
	return bestI
}
