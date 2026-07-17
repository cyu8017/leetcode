// LeetCode 1782 - Count Pairs Of Nodes
// https://leetcode.com/problems/count-pairs-of-nodes/

import "sort"

func countPairs(n int, edges [][]int, queries []int) []int {
	deg := make([]int, n+1)
	shared := make(map[int]int)
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		if a > b {
			a, b = b, a
		}
		deg[a]++
		deg[b]++
		shared[a*100000+b]++
	}
	sortedDeg := make([]int, n)
	copy(sortedDeg, deg[1:])
	sort.Ints(sortedDeg)
	ans := make([]int, 0, len(queries))
	for _, q := range queries {
		res := 0
		left, right := 0, n-1
		for left < right {
			if sortedDeg[left]+sortedDeg[right] > q {
				res += right - left
				right--
			} else {
				left++
			}
		}
		for key, count := range shared {
			a, b := key/100000, key%100000
			sum := deg[a] + deg[b]
			if sum > q && q >= sum-count {
				res--
			}
		}
		ans = append(ans, res)
	}
	return ans
}
