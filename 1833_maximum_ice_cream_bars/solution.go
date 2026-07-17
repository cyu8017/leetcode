// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

import "sort"

func maxIceCream(costs []int, coins int) int {
	sort.Ints(costs)
	count := 0
	for _, cost := range costs {
		if coins < cost {
			break
		}
		coins -= cost
		count++
	}
	return count
}
