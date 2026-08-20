// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

import "sort"

func findOriginalArray(changed []int) []int {
	if len(changed)%2 != 0 {
		return []int{}
	}
	sort.Ints(changed)
	freq := map[int]int{}
	for _, x := range changed {
		freq[x]++
	}
	ans := []int{}
	for _, x := range changed {
		if freq[x] == 0 {
			continue
		}
		freq[x]--
		if freq[2*x] == 0 {
			return []int{}
		}
		freq[2*x]--
		ans = append(ans, x)
	}
	return ans
}
