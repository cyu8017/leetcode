// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	free := 0
	hold := -prices[0]
	cooldown := 0
	for _, price := range prices[1:] {
		nextFree := free
		if cooldown > nextFree {
			nextFree = cooldown
		}
		nextHold := hold
		if free-price > nextHold {
			nextHold = free - price
		}
		nextCooldown := hold + price
		free = nextFree
		hold = nextHold
		cooldown = nextCooldown
	}
	if cooldown > free {
		return cooldown
	}
	return free
}
