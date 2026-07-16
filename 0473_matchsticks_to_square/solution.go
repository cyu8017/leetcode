// LeetCode 0473 - Matchsticks to Square
// https://leetcode.com/problems/matchsticks-to-square/

import "sort"

func dfs(index, side int, matchsticks []int, sides []int) bool {
	if index == len(matchsticks) {
		return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side
	}

	length := matchsticks[index]
	for sideIndex := 0; sideIndex < 4; sideIndex++ {
		if sides[sideIndex]+length > side {
			continue
		}
		if sideIndex > 0 && sides[sideIndex] == sides[sideIndex-1] {
			continue
		}
		sides[sideIndex] += length
		if dfs(index+1, side, matchsticks, sides) {
			return true
		}
		sides[sideIndex] -= length
	}
	return false
}

func makesquare(matchsticks []int) bool {
	if len(matchsticks) == 0 {
		return false
	}
	total := 0
	for _, length := range matchsticks {
		total += length
	}
	if total%4 != 0 {
		return false
	}
	side := total / 4
	sort.Sort(sort.Reverse(sort.IntSlice(matchsticks)))
	sides := []int{0, 0, 0, 0}
	return dfs(0, side, matchsticks, sides)
}
