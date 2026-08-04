// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

func maxScoreWords(words []string, letters []byte, score []int) int {
	available := [26]int{}
	for _, ch := range letters {
		available[ch-'a']++
	}
	counts := make([][26]int, len(words))
	values := make([]int, len(words))
	for i, word := range words {
		for j := 0; j < len(word); j++ {
			counts[i][word[j]-'a']++
			values[i] += score[word[j]-'a']
		}
	}
	var dfs func(int) int
	dfs = func(i int) int {
		if i == len(words) {
			return 0
		}
		best := dfs(i + 1)
		ok := true
		for c := 0; c < 26; c++ {
			if counts[i][c] > available[c] {
				ok = false
				break
			}
		}
		if ok {
			for c := 0; c < 26; c++ {
				available[c] -= counts[i][c]
			}
			v := values[i] + dfs(i+1)
			if v > best {
				best = v
			}
			for c := 0; c < 26; c++ {
				available[c] += counts[i][c]
			}
		}
		return best
	}
	return dfs(0)
}
