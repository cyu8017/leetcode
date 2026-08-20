// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

func isGood(nums []int) bool {
	n := len(nums) - 1
	if n < 1 {
		return false
	}
	freq := make([]int, n+1)
	for _, v := range nums {
		if v < 1 || v > n {
			return false
		}
		freq[v]++
	}
	for i := 1; i < n; i++ {
		if freq[i] != 1 {
			return false
		}
	}
	return freq[n] == 2
}
