// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

func minOperations(nums []int) int {
	freq := map[int]int{}
	for _, v := range nums {
		freq[v]++
	}
	ans := 0
	for _, c := range freq {
		if c == 1 {
			return -1
		}
		ans += (c + 2) / 3
	}
	return ans
}
