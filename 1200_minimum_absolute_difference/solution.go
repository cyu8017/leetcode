// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

import "sort"

func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	best := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] < best {
			best = arr[i] - arr[i-1]
		}
	}
	ans := [][]int{}
	for i := 1; i < len(arr); i++ {
		if arr[i]-arr[i-1] == best {
			ans = append(ans, []int{arr[i-1], arr[i]})
		}
	}
	return ans
}
