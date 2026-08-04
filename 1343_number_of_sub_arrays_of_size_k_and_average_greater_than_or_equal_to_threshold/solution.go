// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

func numOfSubarrays(arr []int, k int, threshold int) int {
	window := 0
	for i := 0; i < k; i++ {
		window += arr[i]
	}
	answer := 0
	if window >= k*threshold {
		answer = 1
	}
	for i := k; i < len(arr); i++ {
		window += arr[i] - arr[i-k]
		if window >= k*threshold {
			answer++
		}
	}
	return answer
}
