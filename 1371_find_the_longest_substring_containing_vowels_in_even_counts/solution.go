// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

func findTheLongestSubstring(s string) int {
	first := map[int]int{0: -1}
	mask, ans := 0, 0
	vowels := "aeiou"
	for i := 0; i < len(s); i++ {
		for j := 0; j < 5; j++ {
			if s[i] == vowels[j] {
				mask ^= 1 << j
			}
		}
		if idx, ok := first[mask]; ok {
			if i-idx > ans {
				ans = i - idx
			}
		} else {
			first[mask] = i
		}
	}
	return ans
}
