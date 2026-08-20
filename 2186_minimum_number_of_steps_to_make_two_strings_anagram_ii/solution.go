// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

func minSteps(s string, t string) int {
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	for i := 0; i < len(t); i++ {
		freq[t[i]-'a']--
	}
	ans := 0
	for _, v := range freq {
		if v > 0 {
			ans += v
		} else {
			ans -= v
		}
	}
	return ans
}
