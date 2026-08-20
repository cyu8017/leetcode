// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

func uniqueLetterString(s string) int {
	n := len(s)
	last := map[byte][]int{}
	for i := 0; i < n; i++ {
		ch := s[i]
		if _, ok := last[ch]; !ok {
			last[ch] = []int{-1}
		}
	}
	for i := 0; i < n; i++ {
		last[s[i]] = append(last[s[i]], i)
	}
	for ch := range last {
		last[ch] = append(last[ch], n)
	}
	ans := 0
	for _, indices := range last {
		for k := 1; k < len(indices)-1; k++ {
			ans += (indices[k] - indices[k-1]) * (indices[k+1] - indices[k])
		}
	}
	return ans
}
