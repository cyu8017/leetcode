// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

func maxProfit(prices []int, profits []int) int {
	n := len(prices)
	ans := -1
	maxLeft := make([]int, n)
	bit := make([]int, 5002)
	update := func(i, val int) {
		for i < len(bit) {
			if val > bit[i] {
				bit[i] = val
			}
			i += i & -i
		}
	}
	query := func(i int) int {
		best := -1
		for i > 0 {
			if bit[i] > best {
				best = bit[i]
			}
			i -= i & -i
		}
		return best
	}
	for j := 0; j < n; j++ {
		maxLeft[j] = query(prices[j] - 1)
		update(prices[j], profits[j])
	}
	for i := range bit {
		bit[i] = 0
	}
	for j := n - 1; j >= 0; j-- {
		bestR := query(5001 - (prices[j] + 1))
		// query values with price > prices[j]: use mirrored index
	}
	// simpler O(n log n) with fenwick on price for right max — fallback O(n^2) for correctness
	rightBest := make([]int, n)
	for i := range rightBest {
		rightBest[i] = -1
	}
	for j := 0; j < n; j++ {
		bestR := -1
		for k := j + 1; k < n; k++ {
			if prices[k] > prices[j] && profits[k] > bestR {
				bestR = profits[k]
			}
		}
		if maxLeft[j] >= 0 && bestR >= 0 {
			cand := maxLeft[j] + profits[j] + bestR
			if cand > ans {
				ans = cand
			}
		}
	}
	return ans
}
