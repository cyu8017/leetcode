// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

import "sort"

func maxCoins(piles []int) int {
	sort.Ints(piles)
	ans := 0
	for i := len(piles) / 3; i < len(piles); i += 2 {
		ans += piles[i]
	}
	return ans
}
