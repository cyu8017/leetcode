// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

import "sort"
import "strings"

func generateSentences(synonyms [][]string, text string) []string {
	parent := map[string]string{}
	var find func(string) string
	find = func(x string) string {
		if _, ok := parent[x]; !ok {
			parent[x] = x
		}
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	for _, pair := range synonyms {
		ra, rb := find(pair[0]), find(pair[1])
		parent[ra] = rb
	}
	groups := map[string][]string{}
	for word := range parent {
		r := find(word)
		groups[r] = append(groups[r], word)
	}
	for r := range groups {
		sort.Strings(groups[r])
	}
	words := strings.Fields(text)
	choices := make([][]string, len(words))
	for i, w := range words {
		if _, ok := parent[w]; ok {
			choices[i] = groups[find(w)]
		} else {
			choices[i] = []string{w}
		}
	}
	ans := []string{}
	var dfs func(int, []string)
	dfs = func(i int, cur []string) {
		if i == len(choices) {
			ans = append(ans, strings.Join(cur, " "))
			return
		}
		for _, w := range choices[i] {
			dfs(i+1, append(cur, w))
		}
	}
	dfs(0, nil)
	return ans
}
