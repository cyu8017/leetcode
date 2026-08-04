// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

import "sort"

func splitPainting(segments [][]int) [][]int64 {
	diff := make(map[int]int64)
	for _, seg := range segments {
		diff[seg[0]] += int64(seg[2])
		diff[seg[1]] -= int64(seg[2])
	}
	points := make([]int, 0, len(diff))
	for p := range diff {
		points = append(points, p)
	}
	sort.Ints(points)
	ans := [][]int64{}
	var cur int64
	for i := 0; i < len(points)-1; i++ {
		cur += diff[points[i]]
		if cur != 0 {
			ans = append(ans, []int64{int64(points[i]), int64(points[i+1]), cur})
		}
	}
	return ans
}
