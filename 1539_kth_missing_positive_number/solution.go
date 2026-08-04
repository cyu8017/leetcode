// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

func findKthPositive(arr []int, k int) int {
	left, right := 0, len(arr)
	for left < right {
		middle := (left + right) / 2
		if arr[middle]-middle-1 < k {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return left + k
}
