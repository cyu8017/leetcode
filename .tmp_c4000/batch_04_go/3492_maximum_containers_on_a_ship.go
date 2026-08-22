// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

func maxContainers(n int, w int, maxWeight int) int {
	cap := n * n
	byW := maxWeight / w
	if cap < byW {
		return cap
	}
	return byW
}
