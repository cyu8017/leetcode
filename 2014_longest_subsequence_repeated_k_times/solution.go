// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

func longestSubsequenceRepeatedK(s string, k int) string {
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	chars := []byte{}
	for c := 25; c >= 0; c-- {
		if freq[c] >= k {
			chars = append(chars, byte('a'+c))
		}
	}
	isSubseq := func(t string) bool {
		need := 0
		times := 0
		for i := 0; i < len(s); i++ {
			if s[i] == t[need] {
				need++
				if need == len(t) {
					times++
					if times == k {
						return true
					}
					need = 0
				}
			}
		}
		return false
	}
	best := ""
	queue := []string{""}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, ch := range chars {
			nxt := cur + string(ch)
			if isSubseq(nxt) {
				if len(nxt) > len(best) || (len(nxt) == len(best) && nxt > best) {
					best = nxt
				}
				queue = append(queue, nxt)
			}
		}
	}
	return best
}
