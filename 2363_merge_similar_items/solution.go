// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

import "sort"

func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
	mp := map[int]int{}
	for _, it := range items1 {
		mp[it[0]] += it[1]
	}
	for _, it := range items2 {
		mp[it[0]] += it[1]
	}
	keys := make([]int, 0, len(mp))
	for k := range mp {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	ans := make([][]int, len(keys))
	for i, k := range keys {
		ans[i] = []int{k, mp[k]}
	}
	return ans
}
