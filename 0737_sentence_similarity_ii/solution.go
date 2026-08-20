// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

func areSentencesSimilarTwo(sentence1 []string, sentence2 []string, similarPairs [][]string) bool {
	if len(sentence1) != len(sentence2) {
		return false
	}
	parent := map[string]string{}
	var find func(x string) string
	find = func(x string) string {
		if _, ok := parent[x]; !ok {
			parent[x] = x
		}
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b string) {
		parent[find(a)] = find(b)
	}
	for _, p := range similarPairs {
		union(p[0], p[1])
	}
	for i := range sentence1 {
		if find(sentence1[i]) != find(sentence2[i]) {
			return false
		}
	}
	return true
}
