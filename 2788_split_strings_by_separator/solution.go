// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

func splitWordsBySeparator(words []string, separator string) []string {
	ans := []string{}
	sep := separator[0]
	for _, w := range words {
		start := 0
		for i := 0; i <= len(w); i++ {
			if i == len(w) || w[i] == sep {
				if i > start {
					ans = append(ans, w[start:i])
				}
				start = i + 1
			}
		}
	}
	return ans
}
