// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

func letterCasePermutation(s string) []string {
	result := []string{""}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		next := []string{}
		if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') {
			lower := ch | 32
			upper := ch &^ 32
			for _, prefix := range result {
				next = append(next, prefix+string(lower), prefix+string(upper))
			}
		} else {
			for _, prefix := range result {
				next = append(next, prefix+string(ch))
			}
		}
		result = next
	}
	return result
}
