// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

import "sort"

func makeSimilar(nums []int, target []int) int64 {
	sort.Ints(nums)
	sort.Ints(target)
	var oddN, evenN, oddT, evenT []int
	for _, x := range nums {
		if x%2 == 0 {
			evenN = append(evenN, x)
		} else {
			oddN = append(oddN, x)
		}
	}
	for _, x := range target {
		if x%2 == 0 {
			evenT = append(evenT, x)
		} else {
			oddT = append(oddT, x)
		}
	}
	var ans int64
	for i := range oddN {
		diff := oddN[i] - oddT[i]
		if diff > 0 {
			ans += int64(diff) / 2
		}
	}
	for i := range evenN {
		diff := evenN[i] - evenT[i]
		if diff > 0 {
			ans += int64(diff) / 2
		}
	}
	return ans
}
