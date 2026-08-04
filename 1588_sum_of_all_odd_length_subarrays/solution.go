// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

func sumOddLengthSubarrays(arr []int) int {
	n := len(arr)
	ans := 0
	for i, x := range arr {
		ans += x * (((i+1)*(n-i) + 1) / 2)
	}
	return ans
}
