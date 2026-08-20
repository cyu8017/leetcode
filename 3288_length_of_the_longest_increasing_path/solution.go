// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

import "sort"

func maxPathLength(coordinates [][]int, k int) int {
	n := len(coordinates)
	type pt struct{ x, y, i int }
	arr := make([]pt, n)
	for i, c := range coordinates {
		arr[i] = pt{c[0], c[1], i}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].x == arr[j].x {
			return arr[i].y > arr[j].y
		}
		return arr[i].x < arr[j].x
	})
	// LIS on y for points before and after k
	kx, ky := coordinates[k][0], coordinates[k][1]
	left, right := []int{}, []int{}
	for _, p := range arr {
		if p.x < kx && p.y < ky {
			left = append(left, p.y)
		}
		if p.x > kx && p.y > ky {
			right = append(right, p.y)
		}
	}
	return lis(left) + 1 + lis(right)
}

func lis(a []int) int {
	tails := []int{}
	for _, x := range a {
		i := sort.SearchInts(tails, x)
		if i == len(tails) {
			tails = append(tails, x)
		} else {
			tails[i] = x
		}
	}
	return len(tails)
}
