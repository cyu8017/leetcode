// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/


func maximumNumberOfStringPairs(words []string) int {
	seen := map[string]bool{}
	ans := 0
	for _, w := range words {
		rev := string([]byte{w[1], w[0]})
		if seen[rev] {
			ans++
			delete(seen, rev)
		} else {
			seen[w] = true
		}
	}
	return ans
}
