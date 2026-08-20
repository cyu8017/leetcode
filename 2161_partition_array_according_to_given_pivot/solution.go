// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

func pivotArray(nums []int, pivot int) []int {
	less, eq, greater := []int{}, []int{}, []int{}
	for _, x := range nums {
		if x < pivot {
			less = append(less, x)
		} else if x == pivot {
			eq = append(eq, x)
		} else {
			greater = append(greater, x)
		}
	}
	return append(append(less, eq...), greater...)
}
