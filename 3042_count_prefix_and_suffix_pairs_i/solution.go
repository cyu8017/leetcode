// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

func countPrefixSuffixPairs(words []string) (ans int) {
	for i, s := range words {
		for _, t := range words[i+1:] {
			if strings.HasPrefix(t, s) && strings.HasSuffix(t, s) {
				ans++
			}
		}
	}
	return
}
