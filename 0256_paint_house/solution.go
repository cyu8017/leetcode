// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

func minCost(costs [][]int) int {
	if len(costs) == 0 {
		return 0
	}
	previous := append([]int(nil), costs[0]...)
	for row := 1; row < len(costs); row++ {
		previous = []int{
			costs[row][0] + min(previous[1], previous[2]),
			costs[row][1] + min(previous[0], previous[2]),
			costs[row][2] + min(previous[0], previous[1]),
		}
	}
	return min(previous[0], previous[1], previous[2])
}
