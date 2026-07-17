// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

import "sort"

func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[i][1] > boxTypes[j][1]
	})
	total := 0
	for _, box := range boxTypes {
		take := box[0]
		if truckSize < take {
			take = truckSize
		}
		total += take * box[1]
		truckSize -= take
		if truckSize == 0 {
			break
		}
	}
	return total
}
