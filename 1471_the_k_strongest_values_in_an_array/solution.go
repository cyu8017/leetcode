// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

import "sort"

func getStrongest(arr []int, k int) []int {
	sort.Ints(arr)
	median := arr[(len(arr)-1)/2]
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	sort.Slice(arr, func(i, j int) bool {
		ai, aj := abs(arr[i]-median), abs(arr[j]-median)
		if ai != aj {
			return ai > aj
		}
		return arr[i] > arr[j]
	})
	return arr[:k]
}
