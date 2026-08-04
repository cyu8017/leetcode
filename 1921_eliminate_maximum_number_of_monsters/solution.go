// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

import "sort"

func eliminateMaximum(dist []int, speed []int) int {
	arrival := make([]int, len(dist))
	for i := range dist {
		arrival[i] = (dist[i] + speed[i] - 1) / speed[i]
	}
	sort.Ints(arrival)
	for i, t := range arrival {
		if t <= i {
			return i
		}
	}
	return len(arrival)
}
