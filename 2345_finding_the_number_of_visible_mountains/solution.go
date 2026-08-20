// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

import "sort"

func visibleMountains(peaks [][]int) int {
	type mt struct{ l, r int }
	arr := make([]mt, len(peaks))
	for i, p := range peaks {
		arr[i] = mt{p[0] - p[1], p[0] + p[1]}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].l == arr[j].l {
			return arr[i].r > arr[j].r
		}
		return arr[i].l < arr[j].l
	})
	ans := 0
	maxR := -1 << 30
	for i := 0; i < len(arr); {
		j := i
		for j < len(arr) && arr[j].l == arr[i].l && arr[j].r == arr[i].r {
			j++
		}
		if arr[i].r > maxR {
			if j-i == 1 {
				ans++
			}
			maxR = arr[i].r
		}
		i = j
	}
	return ans
}
