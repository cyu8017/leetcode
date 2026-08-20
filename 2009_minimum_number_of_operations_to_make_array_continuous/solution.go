// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

import "sort"

func minOperations(nums []int) int {
	n := len(nums)
	sort.Ints(nums)
	uniq := nums[:0]
	for _, x := range nums {
		if len(uniq) == 0 || uniq[len(uniq)-1] != x {
			uniq = append(uniq, x)
		}
	}
	ans := n
	j := 0
	for i := 0; i < len(uniq); i++ {
		for j < len(uniq) && uniq[j]-uniq[i]+1 <= n {
			j++
		}
		have := j - i
		if n-have < ans {
			ans = n - have
		}
	}
	return ans
}
