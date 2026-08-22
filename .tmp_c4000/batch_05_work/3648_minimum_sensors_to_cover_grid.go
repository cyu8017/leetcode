// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

func minSensors(n int, m int, k int) int {
	cover := 2*k + 1
	return ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
}
