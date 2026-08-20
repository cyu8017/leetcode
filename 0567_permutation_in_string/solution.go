// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

func checkInclusion(s1 string, s2 string) bool {
	need := len(s1)
	if need > len(s2) {
		return false
	}
	var target, window [26]int
	for i := 0; i < need; i++ {
		target[s1[i]-'a']++
	}
	left := 0
	for right := 0; right < len(s2); right++ {
		window[s2[right]-'a']++
		for right-left+1 > need {
			window[s2[left]-'a']--
			left++
		}
		if window == target {
			return true
		}
	}
	return false
}
