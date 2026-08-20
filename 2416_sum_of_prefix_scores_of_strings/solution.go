// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

type trieNode struct {
	child [26]*trieNode
	cnt   int
}

func sumPrefixScores(words []string) []int {
	root := &trieNode{}
	for _, w := range words {
		cur := root
		for i := 0; i < len(w); i++ {
			c := w[i] - 'a'
			if cur.child[c] == nil {
				cur.child[c] = &trieNode{}
			}
			cur = cur.child[c]
			cur.cnt++
		}
	}
	ans := make([]int, len(words))
	for i, w := range words {
		cur := root
		sum := 0
		for j := 0; j < len(w); j++ {
			cur = cur.child[w[j]-'a']
			sum += cur.cnt
		}
		ans[i] = sum
	}
	return ans
}
