// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

import "sort"

func intersection(nums [][]int) []int {
	freq := map[int]int{}
	for _, arr := range nums {
		seen := map[int]bool{}
		for _, x := range arr {
			if !seen[x] {
				freq[x]++
				seen[x] = true
			}
		}
	}
	ans := []int{}
	for x, c := range freq {
		if c == len(nums) {
			ans = append(ans, x)
		}
	}
	sort.Ints(ans)
	return ans
}
