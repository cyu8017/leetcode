// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

import "sort"

func canDistribute(nums []int, quantity []int) bool {
	freq := map[int]int{}
	for _, v := range nums {
		freq[v]++
	}
	cnt := make([]int, 0, len(freq))
	for _, c := range freq {
		cnt = append(cnt, c)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(quantity)))
	m := len(quantity)
	sums := make([]int, 1<<m)
	for mask := 1; mask < 1<<m; mask++ {
		bit := mask & -mask
		sums[mask] = sums[mask^bit] + quantity[bitLength(bit)-1]
	}
	dp := map[int]bool{0: true}
	for _, c := range cnt {
		nxt := map[int]bool{}
		for mask := range dp {
			nxt[mask] = true
			left := ((1 << m) - 1) ^ mask
			for sub := left; sub > 0; sub = (sub - 1) & left {
				if sums[sub] <= c {
					nxt[mask|sub] = true
				}
			}
		}
		dp = nxt
	}
	return dp[(1<<m)-1]
}

func bitLength(x int) int {
	n := 0
	for x > 0 {
		x >>= 1
		n++
	}
	return n
}
