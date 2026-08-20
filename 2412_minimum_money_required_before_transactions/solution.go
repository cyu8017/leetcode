// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

func minimumMoney(transactions [][]int) int64 {
	var totalLoss, maxCashback, maxCost int64
	for _, t := range transactions {
		cost, cashback := int64(t[0]), int64(t[1])
		if cost > cashback {
			totalLoss += cost - cashback
			if cashback > maxCashback {
				maxCashback = cashback
			}
		} else if cost > maxCost {
			maxCost = cost
		}
	}
	a := totalLoss + maxCashback
	b := totalLoss + maxCost
	if a > b {
		return a
	}
	return b
}
