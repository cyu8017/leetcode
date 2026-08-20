// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

import "sort"

func maxIntersectionCount(y []int) int {
	n := len(y)
	line := map[int]int{}
	for i := 1; i < n; i++ {
		start := 2 * y[i-1]
		end := 2 * y[i]
		if i != n-1 {
			if y[i] > y[i-1] {
				end--
			} else {
				end++
			}
		}
		a, b := start, end
		if a > b {
			a, b = b, a
		}
		line[a]++
		line[b+1]--
	}
	keys := make([]int, 0, len(line))
	for k := range line {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	ans, cur := 0, 0
	for _, k := range keys {
		cur += line[k]
		if cur > ans {
			ans = cur
		}
	}
	return ans
}
