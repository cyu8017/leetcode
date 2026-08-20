// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

import "sort"

func maximumImportance(n int, roads [][]int) int64 {
	deg := make([]int, n)
	for _, r := range roads {
		deg[r[0]]++
		deg[r[1]]++
	}
	sort.Ints(deg)
	var ans int64
	for i := 0; i < n; i++ {
		ans += int64(deg[i]) * int64(i+1)
	}
	return ans
}
