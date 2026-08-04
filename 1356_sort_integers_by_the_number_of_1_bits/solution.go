// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

import "sort"

func sortByBits(arr []int) []int {
	bits := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	sort.Slice(arr, func(i, j int) bool {
		bi, bj := bits(arr[i]), bits(arr[j])
		if bi != bj {
			return bi < bj
		}
		return arr[i] < arr[j]
	})
	return arr
}
