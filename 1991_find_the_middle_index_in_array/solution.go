// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

func findMiddleIndex(nums []int) int {
	total := 0
	for _, x := range nums {
		total += x
	}
	left := 0
	for i, x := range nums {
		if left == total-left-x {
			return i
		}
		left += x
	}
	return -1
}
