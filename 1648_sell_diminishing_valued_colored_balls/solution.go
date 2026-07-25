// LeetCode 1648 - Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

import "sort"

func maxProfit(inventory []int, orders int) int {
	const mod = 1000000007
	sort.Sort(sort.Reverse(sort.IntSlice(inventory)))
	inventory = append(inventory, 0)
	ans := 0
	for i := 0; i+1 < len(inventory); i++ {
		width := int64(i + 1)
		high, low := int64(inventory[i]), int64(inventory[i+1])
		balls := width * (high - low)
		take := int64(orders)
		if balls < take {
			take = balls
		}
		full := take / width
		rem := take % width
		bottom := high - full
		ans = (ans + int(width*(high+bottom+1)*full/2%mod+rem*bottom%mod)) % mod
		orders -= int(take)
		if orders == 0 {
			break
		}
	}
	return ans
}
