// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

func smallestSubsequence(s string) string {
	last := map[byte]int{}
	for i := 0; i < len(s); i++ {
		last[s[i]] = i
	}
	stack := []byte{}
	used := map[byte]bool{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if used[ch] {
			continue
		}
		for len(stack) > 0 && ch < stack[len(stack)-1] && last[stack[len(stack)-1]] > i {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			delete(used, top)
		}
		stack = append(stack, ch)
		used[ch] = true
	}
	return string(stack)
}
