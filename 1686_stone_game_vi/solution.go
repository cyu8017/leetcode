// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

import "sort"

func stoneGameVI(aliceValues, bobValues []int) int {
	n := len(aliceValues)
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		return aliceValues[order[i]]+bobValues[order[i]] > aliceValues[order[j]]+bobValues[order[j]]
	})
	score := 0
	for t, i := range order {
		if t%2 == 0 {
			score += aliceValues[i]
		} else {
			score -= bobValues[i]
		}
	}
	if score > 0 {
		return 1
	}
	if score < 0 {
		return -1
	}
	return 0
}
