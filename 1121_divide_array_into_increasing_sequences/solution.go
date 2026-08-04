// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

func canDivideIntoSubsequences(nums []int, k int) bool {
	freq := map[int]int{}
	maxFreq := 0
	for _, x := range nums {
		freq[x]++
		if freq[x] > maxFreq {
			maxFreq = freq[x]
		}
	}
	return len(nums) >= k*maxFreq
}
