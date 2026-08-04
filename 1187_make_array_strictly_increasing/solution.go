// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

import "sort"

func makeArrayIncreasing(arr1 []int, arr2 []int) int {
	set := map[int]bool{}
	for _, x := range arr2 {
		set[x] = true
	}
	uniq := make([]int, 0, len(set))
	for x := range set {
		uniq = append(uniq, x)
	}
	sort.Ints(uniq)
	arr2 = uniq
	const inf = int(^uint(0) >> 1)
	dp := map[int]int{-1: 0}
	for _, num := range arr1 {
		newDP := map[int]int{}
		for prev, ops := range dp {
			if num > prev {
				if cur, ok := newDP[num]; !ok || ops < cur {
					newDP[num] = ops
				}
			}
			idx := sort.SearchInts(arr2, prev+1)
			if idx < len(arr2) {
				chosen := arr2[idx]
				if cur, ok := newDP[chosen]; !ok || ops+1 < cur {
					newDP[chosen] = ops + 1
				}
			}
		}
		dp = newDP
		if len(dp) == 0 {
			return -1
		}
	}
	best := inf
	for _, v := range dp {
		if v < best {
			best = v
		}
	}
	return best
}
