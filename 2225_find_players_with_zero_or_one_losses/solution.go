// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

import "sort"

func findWinners(matches [][]int) [][]int {
	lose := map[int]int{}
	seen := map[int]bool{}
	for _, m := range matches {
		seen[m[0]] = true
		seen[m[1]] = true
		lose[m[1]]++
	}
	zero, one := []int{}, []int{}
	for p := range seen {
		if lose[p] == 0 {
			zero = append(zero, p)
		} else if lose[p] == 1 {
			one = append(one, p)
		}
	}
	sort.Ints(zero)
	sort.Ints(one)
	return [][]int{zero, one}
}
