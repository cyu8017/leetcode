// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

import "sort"

func shortestDistanceColor(colors []int, queries [][]int) []int {
	pos := map[int][]int{}
	for i, c := range colors {
		pos[c] = append(pos[c], i)
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		i, c := q[0], q[1]
		arr, ok := pos[c]
		if !ok {
			ans[qi] = -1
			continue
		}
		idx := sort.SearchInts(arr, i)
		best := int(^uint(0) >> 1)
		if idx < len(arr) && arr[idx]-i < best {
			best = arr[idx] - i
		}
		if idx > 0 && i-arr[idx-1] < best {
			best = i - arr[idx-1]
		}
		if best == int(^uint(0)>>1) {
			ans[qi] = -1
		} else {
			ans[qi] = best
		}
	}
	return ans
}
