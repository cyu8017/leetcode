// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

func indexPairs(text string, words []string) [][]int {
	wordSet := map[string]bool{}
	for _, w := range words {
		wordSet[w] = true
	}
	ans := [][]int{}
	n := len(text)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if wordSet[text[i:j+1]] {
				ans = append(ans, []int{i, j})
			}
		}
	}
	return ans
}
