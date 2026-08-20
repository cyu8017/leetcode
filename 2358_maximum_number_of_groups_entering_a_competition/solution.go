// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

func maximumGroups(grades []int) int {
	n := len(grades)
	k := 0
	for (k+1)*(k+2)/2 <= n {
		k++
	}
	return k
}
