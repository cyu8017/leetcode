// LeetCode 1196 - How Many Apples Can You Put into the Basket
// https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

import "sort"

func maxNumberOfApples(weight []int) int {
	sort.Ints(weight)
	total := 0
	for i, w := range weight {
		total += w
		if total > 5000 {
			return i
		}
	}
	return len(weight)
}
