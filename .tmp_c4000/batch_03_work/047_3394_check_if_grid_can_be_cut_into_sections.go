// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

import "sort"

func checkValidCuts(n int, rectangles [][]int) bool {
	return checkCut(rectangles, 0) || checkCut(rectangles, 1)
}

func checkCut(rects [][]int, axis int) bool {
	type seg struct{ a, b int }
	arr := make([]seg, len(rects))
	for i, r := range rects {
		if axis == 0 {
			arr[i] = seg{r[0], r[2]}
		} else {
			arr[i] = seg{r[1], r[3]}
		}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].a == arr[j].a {
			return arr[i].b < arr[j].b
		}
		return arr[i].a < arr[j].a
	})
	cuts := 0
	end := arr[0].b
	for i := 1; i < len(arr); i++ {
		if arr[i].a >= end {
			cuts++
			end = arr[i].b
			if cuts >= 2 {
				return true
			}
		} else if arr[i].b > end {
			end = arr[i].b
		}
	}
	return false
}
