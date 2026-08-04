// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

import "sort"

func maxBoxesInWarehouse(boxes []int, warehouse []int) int {
	for i := 1; i < len(warehouse); i++ {
		if warehouse[i] > warehouse[i-1] {
			warehouse[i] = warehouse[i-1]
		}
	}
	sort.Ints(boxes)
	room, used := len(warehouse)-1, 0
	for _, box := range boxes {
		for room >= 0 && warehouse[room] < box {
			room--
		}
		if room < 0 {
			break
		}
		used++
		room--
	}
	return used
}
