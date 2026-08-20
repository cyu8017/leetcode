// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

import "sort"

func deckRevealedIncreasing(deck []int) []int {
	sort.Ints(deck)
	n := len(deck)
	idx := make([]int, n)
	for i := 0; i < n; i++ {
		idx[i] = i
	}
	ans := make([]int, n)
	for _, card := range deck {
		ans[idx[0]] = card
		idx = idx[1:]
		if len(idx) > 0 {
			idx = append(idx, idx[0])
			idx = idx[1:]
		}
	}
	return ans
}
