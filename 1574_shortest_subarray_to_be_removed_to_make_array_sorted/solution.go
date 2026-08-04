// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
	right := n - 1
	for right > 0 && arr[right-1] <= arr[right] {
		right--
	}
	if right == 0 {
		return 0
	}
	answer, left := right, 0
	for {
		for right < n && arr[right] < arr[left] {
			right++
		}
		if right-left-1 < answer {
			answer = right - left - 1
		}
		left++
		if left >= n || (left > 0 && arr[left-1] > arr[left]) {
			break
		}
	}
	return answer
}
