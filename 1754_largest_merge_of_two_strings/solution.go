// LeetCode 1754 - Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/

func largestMerge(word1 string, word2 string) string {
	i, j := 0, 0
	out := make([]byte, 0, len(word1)+len(word2))
	for i < len(word1) && j < len(word2) {
		if word1[i:] > word2[j:] {
			out = append(out, word1[i])
			i++
		} else {
			out = append(out, word2[j])
			j++
		}
	}
	out = append(out, word1[i:]...)
	out = append(out, word2[j:]...)
	return string(out)
}
