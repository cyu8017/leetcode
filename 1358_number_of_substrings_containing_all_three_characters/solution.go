// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

func numberOfSubstrings(s string) int {
	count := [3]int{}
	left, answer := 0, 0
	for right := 0; right < len(s); right++ {
		count[s[right]-'a']++
		for count[0] > 0 && count[1] > 0 && count[2] > 0 {
			answer += len(s) - right
			count[s[left]-'a']--
			left++
		}
	}
	return answer
}
