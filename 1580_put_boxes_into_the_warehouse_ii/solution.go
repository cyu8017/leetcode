// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

import "sort"

func maxBoxesInWarehouse(boxes []int, warehouse []int) int {
	n := len(warehouse)
	left := append([]int{}, warehouse...)
	right := append([]int{}, warehouse...)
	for i := 1; i < n; i++ {
		if left[i] > left[i-1] {
			left[i] = left[i-1]
		}
	}
	for i := n - 2; i >= 0; i-- {
		if right[i] > right[i+1] {
			right[i] = right[i+1]
		}
	}
	capacity := make([]int, n)
	for i := 0; i < n; i++ {
		if left[i] > right[i] {
			capacity[i] = left[i]
		} else {
			capacity[i] = right[i]
		}
	}
	sort.Ints(capacity)
	sort.Ints(boxes)
	i := 0
	for _, room := range capacity {
		if i < len(boxes) && boxes[i] <= room {
			i++
		}
	}
	return i
}
