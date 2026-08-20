// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

import "sort"

func sumImbalanceNumbers(nums []int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		seen := map[int]bool{}
		sortedVals := []int{}
		imbalance := 0
		for j := i; j < n; j++ {
			x := nums[j]
			if !seen[x] {
				seen[x] = true
				pos := sort.SearchInts(sortedVals, x)
				leftOk, rightOk := false, false
				if pos > 0 {
					if x-sortedVals[pos-1] == 1 {
						leftOk = true
					} else {
						imbalance++
					}
				}
				if pos < len(sortedVals) {
					if sortedVals[pos]-x == 1 {
						rightOk = true
					} else {
						imbalance++
					}
				}
				if pos > 0 && pos < len(sortedVals) {
					if sortedVals[pos]-sortedVals[pos-1] > 1 {
						imbalance--
					}
				}
				_ = leftOk
				_ = rightOk
				sortedVals = append(sortedVals, 0)
				copy(sortedVals[pos+1:], sortedVals[pos:])
				sortedVals[pos] = x
			}
			ans += imbalance
		}
	}
	return ans
}
