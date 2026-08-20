// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

func wordSubsets(words1 []string, words2 []string) []string {
	need := [26]int{}
	for _, w := range words2 {
		cur := [26]int{}
		for _, ch := range w {
			cur[ch-'a']++
		}
		for i := 0; i < 26; i++ {
			if cur[i] > need[i] {
				need[i] = cur[i]
			}
		}
	}
	ans := []string{}
	for _, w := range words1 {
		cur := [26]int{}
		for _, ch := range w {
			cur[ch-'a']++
		}
		ok := true
		for i := 0; i < 26; i++ {
			if cur[i] < need[i] {
				ok = false
				break
			}
		}
		if ok {
			ans = append(ans, w)
		}
	}
	return ans
}
