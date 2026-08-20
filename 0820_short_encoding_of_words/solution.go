// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

func minimumLengthEncoding(words []string) int {
	good := map[string]bool{}
	for _, w := range words {
		good[w] = true
	}
	for _, word := range words {
		for i := 1; i < len(word); i++ {
			delete(good, word[i:])
		}
	}
	ans := 0
	for word := range good {
		ans += len(word) + 1
	}
	return ans
}
