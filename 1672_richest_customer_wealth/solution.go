// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

func maximumWealth(accounts [][]int) int {
	best := 0
	for _, row := range accounts {
		sum := 0
		for _, v := range row {
			sum += v
		}
		if sum > best {
			best = sum
		}
	}
	return best
}
