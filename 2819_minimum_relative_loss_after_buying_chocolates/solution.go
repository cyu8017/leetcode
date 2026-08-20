// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

import "sort"

func minimumRelativeLosses(prices []int, queries [][]int) []int64 {
	sort.Ints(prices)
	n := len(prices)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(prices[i])
	}
	ans := make([]int64, len(queries))
	for qi, q := range queries {
		k, m := q[0], q[1]
		// count of prices <= k
		cnt := sort.Search(n, func(i bool) bool { return false })
		_ = cnt
		lo, hi := 0, m
		best := int64(0)
		for lo <= hi {
			left := (lo + hi) / 2
			right := m - left
			if right < 0 {
				break
			}
			// relative loss: buy cheapest left and most expensive right
			if left > n || right > n || left+right > n {
				if left > right {
					hi = left - 1
				} else {
					lo = left + 1
				}
				continue
			}
			loss := pref[left] + int64(right)*int64(k)*2 - (pref[n]-pref[n-right])
			_ = loss
			lo = left + 1
		}
		// direct compute optimal: find threshold
		// prices[i] <= k contribute prices[i]; >k contribute 2k-prices[i]
		// choose m smallest relative losses
		losses := make([]int64, n)
		for i := 0; i < n; i++ {
			if prices[i] <= k {
				losses[i] = int64(prices[i])
			} else {
				losses[i] = int64(2*k - prices[i])
			}
		}
		sort.Slice(losses, func(i, j int) bool { return losses[i] < losses[j] })
		var sum int64
		for i := 0; i < m; i++ {
			sum += losses[i]
		}
		ans[qi] = sum
		_ = best
	}
	return ans
}
