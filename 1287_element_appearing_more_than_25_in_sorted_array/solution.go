// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

func findSpecialInteger(arr []int) int {
	n := len(arr)
	candidates := []int{arr[n/4], arr[n/2], arr[3*n/4]}
	for _, value := range candidates {
		count := 0
		for _, x := range arr {
			if x == value {
				count++
			}
		}
		if count > n/4 {
			return value
		}
	}
	return arr[0]
}
