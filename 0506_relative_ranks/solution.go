// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

import (
	"sort"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	medals := map[int]string{
		1: "Gold Medal",
		2: "Silver Medal",
		3: "Bronze Medal",
	}
	order := make([]int, len(score))
	for index := range order {
		order[index] = index
	}
	sort.Slice(order, func(i, j int) bool {
		return score[order[i]] > score[order[j]]
	})

	result := make([]string, len(score))
	for rank, index := range order {
		label, ok := medals[rank+1]
		if !ok {
			label = strconv.Itoa(rank + 1)
		}
		result[index] = label
	}
	return result
}
