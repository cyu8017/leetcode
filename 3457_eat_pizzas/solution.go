// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

import "sort"

func maxWeight(pizzas []int) int64 {
	sort.Ints(pizzas)
	n := len(pizzas)
	days := n / 4
	var ans int64
	oddDays := (days + 1) / 2
	evenDays := days / 2
	idx := n - 1
	for i := 0; i < oddDays; i++ {
		ans += int64(pizzas[idx])
		idx--
	}
	for i := 0; i < evenDays; i++ {
		idx-- // skip one
		ans += int64(pizzas[idx])
		idx--
	}
	return ans
}
