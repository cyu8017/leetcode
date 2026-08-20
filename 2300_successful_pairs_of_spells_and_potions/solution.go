// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

import "sort"

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Ints(potions)
	ans := make([]int, len(spells))
	m := len(potions)
	for i, spell := range spells {
		lo, hi := 0, m
		for lo < hi {
			mid := (lo + hi) / 2
			if int64(spell)*int64(potions[mid]) >= success {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		ans[i] = m - lo
	}
	return ans
}
