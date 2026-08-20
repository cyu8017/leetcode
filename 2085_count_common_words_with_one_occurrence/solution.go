// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

func countWords(words1 []string, words2 []string) int {
	f1, f2 := map[string]int{}, map[string]int{}
	for _, w := range words1 {
		f1[w]++
	}
	for _, w := range words2 {
		f2[w]++
	}
	ans := 0
	for w, c := range f1 {
		if c == 1 && f2[w] == 1 {
			ans++
		}
	}
	return ans
}
