// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

import "sort"

func largestValsFromLabels(values []int, labels []int, numWanted int, useLimit int) int {
	type item struct{ value, label int }
	items := make([]item, len(values))
	for i := range values {
		items[i] = item{values[i], labels[i]}
	}
	sort.Slice(items, func(i, j int) bool { return items[i].value > items[j].value })
	used := map[int]int{}
	ans, taken := 0, 0
	for _, it := range items {
		if taken == numWanted {
			break
		}
		if used[it.label] < useLimit {
			used[it.label]++
			ans += it.value
			taken++
		}
	}
	return ans
}
