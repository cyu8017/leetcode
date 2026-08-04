// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

import "sort"

func numberOfWeakCharacters(properties [][]int) int {
	sort.Slice(properties, func(i, j int) bool {
		if properties[i][0] != properties[j][0] {
			return properties[i][0] < properties[j][0]
		}
		return properties[i][1] > properties[j][1]
	})
	ans := 0
	maxDef := 0
	for i := len(properties) - 1; i >= 0; i-- {
		if properties[i][1] < maxDef {
			ans++
		} else {
			maxDef = properties[i][1]
		}
	}
	return ans
}
