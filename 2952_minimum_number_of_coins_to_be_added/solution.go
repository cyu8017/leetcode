// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

import "sort"

func minimumAddedCoins(coins []int, target int) int {
	sort.Ints(coins)
	ans := 0
	reach := 0
	i := 0
	for reach < target {
		if i < len(coins) && coins[i] <= reach+1 {
			reach += coins[i]
			i++
		} else {
			reach += reach + 1
			ans++
		}
	}
	return ans
}
