// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

import "strconv"

func countNicePairs(nums []int) int {
	const mod = 1_000_000_007
	freq := make(map[int]int)
	ans := 0

	for _, num := range nums {
		diff := num - rev(num)
		ans = (ans + freq[diff]) % mod
		freq[diff]++
	}

	return ans
}

func rev(x int) int {
	s := []byte(strconv.Itoa(x))
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	v, _ := strconv.Atoi(string(s))
	return v
}
