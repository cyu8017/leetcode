// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/


import "sort"

func sortBy(arr []interface{}, fn func(interface{}) float64) []interface{} {
	out := append([]interface{}{}, arr...)
	sort.Slice(out, func(i, j int) bool { return fn(out[i]) < fn(out[j]) })
	return out
}
