// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

import "sort"

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	hs := append([]int{0, h}, horizontalCuts...)
	vs := append([]int{0, w}, verticalCuts...)
	sort.Ints(hs)
	sort.Ints(vs)
	maxGap := func(arr []int) int {
		best := 0
		for i := 1; i < len(arr); i++ {
			if arr[i]-arr[i-1] > best {
				best = arr[i] - arr[i-1]
			}
		}
		return best
	}
	return int(int64(maxGap(hs)) * int64(maxGap(vs)) % 1000000007)
}
