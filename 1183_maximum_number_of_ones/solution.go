// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

import "sort"

func maximumNumberOfOnes(width int, height int, sideLength int, maxOnes int) int {
	counts := []int{}
	for r := 0; r < sideLength; r++ {
		for c := 0; c < sideLength; c++ {
			rows := (height - r + sideLength - 1) / sideLength
			cols := (width - c + sideLength - 1) / sideLength
			counts = append(counts, rows*cols)
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(counts)))
	ans := 0
	for i := 0; i < maxOnes && i < len(counts); i++ {
		ans += counts[i]
	}
	return ans
}
