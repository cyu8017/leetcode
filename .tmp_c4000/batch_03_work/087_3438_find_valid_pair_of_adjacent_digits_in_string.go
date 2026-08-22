// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

func findValidPair(s string) string {
	freq := [10]int{}
	for _, c := range s {
		freq[c-'0']++
	}
	for i := 0; i+1 < len(s); i++ {
		a, b := int(s[i]-'0'), int(s[i+1]-'0')
		if a != b && freq[a] == a && freq[b] == b {
			return s[i : i+2]
		}
	}
	return ""
}
