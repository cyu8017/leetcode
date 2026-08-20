// LeetCode 2491 - Divide Players Into Teams of Equal Skill
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

import "sort"

func dividePlayers(skill []int) int64 {
	sort.Ints(skill)
	n := len(skill)
	target := skill[0] + skill[n-1]
	var chem int64
	for i := 0; i < n/2; i++ {
		if skill[i]+skill[n-1-i] != target {
			return -1
		}
		chem += int64(skill[i]) * int64(skill[n-1-i])
	}
	return chem
}
