// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

func findWordsContaining(words []string, x string) []int {
	ans := []int{}
	ch := x[0]
	for i, w := range words {
		for j := 0; j < len(w); j++ {
			if w[j] == ch {
				ans = append(ans, i)
				break
			}
		}
	}
	return ans
}
