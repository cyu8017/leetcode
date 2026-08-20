// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

func similarPairs(words []string) int {
	freq := map[[26]bool]int{}
	ans := 0
	for _, w := range words {
		var mask [26]bool
		for i := 0; i < len(w); i++ {
			mask[w[i]-'a'] = true
		}
		ans += freq[mask]
		freq[mask]++
	}
	return ans
}
