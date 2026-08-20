// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

import "sort"

func maxTwoEvents(events [][]int) int {
	sort.Slice(events, func(i, j int) bool { return events[i][0] < events[j][0] })
	n := len(events)
	suffix := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffix[i] = suffix[i+1]
		if events[i][2] > suffix[i] {
			suffix[i] = events[i][2]
		}
	}
	ans := 0
	for i, e := range events {
		if e[2] > ans {
			ans = e[2]
		}
		lo, hi := i+1, n
		for lo < hi {
			mid := (lo + hi) / 2
			if events[mid][0] > e[1] {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		if lo < n && e[2]+suffix[lo] > ans {
			ans = e[2] + suffix[lo]
		}
	}
	return ans
}
