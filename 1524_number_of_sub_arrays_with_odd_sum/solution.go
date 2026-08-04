// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

func numOfSubarrays(arr []int) int {
	counts := [2]int{1, 0}
	parity, answer := 0, 0
	for _, value := range arr {
		parity ^= value & 1
		answer += counts[parity^1]
		counts[parity]++
	}
	return answer % 1000000007
}
