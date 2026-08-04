// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

import "sort"

func longestObstacleCourseAtEachPosition(obstacles []int) []int {
	tails := []int{}
	ans := make([]int, len(obstacles))
	for i, x := range obstacles {
		j := sort.Search(len(tails), func(k int) bool { return tails[k] > x })
		if j == len(tails) {
			tails = append(tails, x)
		} else {
			tails[j] = x
		}
		ans[i] = j + 1
	}
	return ans
}
