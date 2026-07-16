// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

func findRepeatedDnaSequences(s string) []string {
	seen := make(map[string]bool)
	repeated := make(map[string]bool)
	for i := 0; i+10 <= len(s); i++ {
		sequence := s[i : i+10]
		if seen[sequence] {
			repeated[sequence] = true
		} else {
			seen[sequence] = true
		}
	}

	result := make([]string, 0, len(repeated))
	for sequence := range repeated {
		result = append(result, sequence)
	}
	return result
}