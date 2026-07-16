// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

func minTransfers(transactions [][]int) int {
	balances := make(map[int]int)
	for _, transaction := range transactions {
		source, target, amount := transaction[0], transaction[1], transaction[2]
		balances[source] -= amount
		balances[target] += amount
	}

	debts := make([]int, 0)
	for _, balance := range balances {
		if balance != 0 {
			debts = append(debts, balance)
		}
	}

	var dfs func(index int) int
	dfs = func(index int) int {
		for index < len(debts) && debts[index] == 0 {
			index++
		}
		if index == len(debts) {
			return 0
		}
		best := len(debts)
		for nextIndex := index + 1; nextIndex < len(debts); nextIndex++ {
			if int64(debts[index])*int64(debts[nextIndex]) < 0 {
				debts[nextIndex] += debts[index]
				if candidate := 1 + dfs(index+1); candidate < best {
					best = candidate
				}
				debts[nextIndex] -= debts[index]
			}
		}
		return best
	}

	return dfs(0)
}
