// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

import "sort"

func relativeSortArray(arr1 []int, arr2 []int) []int {
	count := map[int]int{}
	for _, x := range arr1 {
		count[x]++
	}
	ans := make([]int, 0, len(arr1))
	for _, x := range arr2 {
		for count[x] > 0 {
			ans = append(ans, x)
			count[x]--
		}
		delete(count, x)
	}
	rest := make([]int, 0, len(count))
	for x := range count {
		rest = append(rest, x)
	}
	sort.Ints(rest)
	for _, x := range rest {
		for count[x] > 0 {
			ans = append(ans, x)
			count[x]--
		}
	}
	return ans
}
