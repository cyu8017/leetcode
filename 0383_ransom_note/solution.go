// LeetCode 0383 - Ransom Note
// https://leetcode.com/problems/ransom-note/

func canConstruct(ransomNote string, magazine string) bool {
	counts := make([]int, 26)

	for _, ch := range magazine {
		counts[ch-'a']++
	}

	for _, ch := range ransomNote {
		if counts[ch-'a'] == 0 {
			return false
		}
		counts[ch-'a']--
	}

	return true
}
