// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

import "sort"

func totalScore(hp int, damage []int, requirement []int) int64 {
	n := len(damage)
	prefix := make([]int64, n+1)
	for i, value := range damage {
		prefix[i+1] = prefix[i] + int64(value)
	}

	answer := int64(n) * int64(n+1) / 2
	for j := 1; j <= n; j++ {
		threshold := prefix[j] + int64(requirement[j-1]-hp)
		invalid := sort.Search(j, func(i int) bool {
			return prefix[i] >= threshold
		})
		answer -= int64(invalid)
	}
	return answer
}