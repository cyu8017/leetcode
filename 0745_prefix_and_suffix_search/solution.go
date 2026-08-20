// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

type WordFilter struct {
	lookup map[string]int
}

func Constructor(words []string) WordFilter {
	lookup := map[string]int{}
	for index, word := range words {
		size := len(word)
		for i := 0; i <= size; i++ {
			for j := 0; j <= size; j++ {
				lookup[word[:i]+"#"+word[j:]] = index
			}
		}
	}
	return WordFilter{lookup: lookup}
}

func (this *WordFilter) F(pref string, suff string) int {
	if v, ok := this.lookup[pref+"#"+suff]; ok {
		return v
	}
	return -1
}
