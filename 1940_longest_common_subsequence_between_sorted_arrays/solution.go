// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

func longestCommonSubsequence(arrays [][]int) []int {
	cnt := make(map[int]int)
	for _, arr := range arrays {
		for _, x := range arr {
			cnt[x]++
		}
	}
	m := len(arrays)
	ans := []int{}
	for _, x := range arrays[0] {
		if cnt[x] == m {
			ans = append(ans, x)
		}
	}
	return ans
}
