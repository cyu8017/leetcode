// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

import "sort"

func findLeastNumOfUniqueInts(arr []int, k int) int {
	countsMap := map[int]int{}
	for _, v := range arr {
		countsMap[v]++
	}
	counts := make([]int, 0, len(countsMap))
	for _, c := range countsMap {
		counts = append(counts, c)
	}
	sort.Ints(counts)
	removed := 0
	for _, count := range counts {
		if k < count {
			break
		}
		k -= count
		removed++
	}
	return len(counts) - removed
}
