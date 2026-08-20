// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

import "sort"

func smallestTrimmedNumbers(nums []string, queries [][]int) []int {
	ans := make([]int, len(queries))
	for qi, q := range queries {
		k, trim := q[0], q[1]
		type pair struct {
			s string
			i int
		}
		arr := make([]pair, len(nums))
		for i, num := range nums {
			arr[i] = pair{num[len(num)-trim:], i}
		}
		sort.SliceStable(arr, func(i, j int) bool {
			if arr[i].s == arr[j].s {
				return arr[i].i < arr[j].i
			}
			return arr[i].s < arr[j].s
		})
		ans[qi] = arr[k-1].i
	}
	return ans
}
