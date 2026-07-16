// LeetCode 0140 - Word Break II
func wordBreak(s string, wordDict []string) []string {
	words := make(map[string]bool)
	for _, word := range wordDict { words[word] = true }
	memo := make(map[int][]string)
	var dfs func(int) []string
	dfs = func(start int) []string {
		if result, ok := memo[start]; ok { return result }
		result := make([]string, 0)
		if start == len(s) { return []string{""} }
		for end := start + 1; end <= len(s); end++ {
			word := s[start:end]
			if !words[word] { continue }
			for _, tail := range dfs(end) {
				if tail == "" { result = append(result, word) } else { result = append(result, word+" "+tail) }
			}
		}
		memo[start] = result
		return result
	}
	return dfs(0)
}