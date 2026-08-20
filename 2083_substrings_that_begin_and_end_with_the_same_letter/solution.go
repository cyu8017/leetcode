// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

func numberOfSubstrings(s string) int64 {
	freq := [26]int64{}
	var ans int64
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
		ans += freq[s[i]-'a']
	}
	return ans
}
