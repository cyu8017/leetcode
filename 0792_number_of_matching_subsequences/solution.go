// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

func numMatchingSubseq(s string, words []string) int {
	waiting := map[byte][]string{}
	for _, word := range words {
		waiting[word[0]] = append(waiting[word[0]], word[1:])
	}
	count := 0
	for i := 0; i < len(s); i++ {
		ch := s[i]
		advance := waiting[ch]
		waiting[ch] = nil
		for _, rest := range advance {
			if rest == "" {
				count++
			} else {
				waiting[rest[0]] = append(waiting[rest[0]], rest[1:])
			}
		}
	}
	return count
}
