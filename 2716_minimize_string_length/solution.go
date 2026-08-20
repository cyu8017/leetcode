// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/


func minimizedStringLength(s string) int {
	seen := [26]bool{}
	for i := 0; i < len(s); i++ {
		seen[s[i]-'a'] = true
	}
	ans := 0
	for _, v := range seen {
		if v {
			ans++
		}
	}
	return ans
}
