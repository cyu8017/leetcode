// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

import "sort"

func trimMean(arr []int) float64 {
	sort.Ints(arr)
	k := len(arr) / 20
	sum := 0
	for i := k; i < len(arr)-k; i++ {
		sum += arr[i]
	}
	return float64(sum) / float64(len(arr)-2*k)
}
