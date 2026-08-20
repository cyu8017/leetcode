// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

func timeRequiredToBuy(tickets []int, k int) int {
	ans := 0
	for i, t := range tickets {
		if i <= k {
			if t < tickets[k] {
				ans += t
			} else {
				ans += tickets[k]
			}
		} else {
			if t < tickets[k] {
				ans += t
			} else {
				ans += tickets[k] - 1
			}
		}
	}
	return ans
}
