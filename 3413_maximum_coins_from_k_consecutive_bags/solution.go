// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

import "sort"

func maximumCoins(coins [][]int, k int) int64 {
	sort.Slice(coins, func(i, j int) bool { return coins[i][0] < coins[j][0] })
	var ans int64
	// sliding on segments
	n := len(coins)
	// prefix coins
	for i := 0; i < n; i++ {
		var sum int64
		j := i
		start := coins[i][0]
		end := start + k - 1
		for j < n && coins[j][0] <= end {
			l := coins[j][0]
			r := coins[j][1]
			if r > end {
				r = end
			}
			if l < start {
				l = start
			}
			if l <= r {
				sum += int64(r-l+1) * int64(coins[j][2])
			}
			j++
		}
		if sum > ans {
			ans = sum
		}
	}
	// also windows ending at segment ends
	for i := 0; i < n; i++ {
		var sum int64
		end := coins[i][1]
		start := end - k + 1
		for j := 0; j <= i; j++ {
			l := coins[j][0]
			r := coins[j][1]
			if l < start {
				l = start
			}
			if r > end {
				r = end
			}
			if l <= r {
				sum += int64(r-l+1) * int64(coins[j][2])
			}
		}
		if sum > ans {
			ans = sum
		}
	}
	return ans
}
