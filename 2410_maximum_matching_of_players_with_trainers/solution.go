// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

import "sort"

func matchPlayersAndTrainers(players []int, trainers []int) int {
	sort.Ints(players)
	sort.Ints(trainers)
	i, j, ans := 0, 0, 0
	for i < len(players) && j < len(trainers) {
		if players[i] <= trainers[j] {
			ans++
			i++
			j++
		} else {
			j++
		}
	}
	return ans
}
