// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

func evaluate(s string, knowledge [][]string) string {
	lookup := make(map[string]string, len(knowledge))
	for _, pair := range knowledge {
		lookup[pair[0]] = pair[1]
	}

	result := make([]byte, 0, len(s))
	i := 0
	for i < len(s) {
		if s[i] == '(' {
			j := i + 1
			for s[j] != ')' {
				j++
			}
			key := s[i+1 : j]
			if value, ok := lookup[key]; ok {
				result = append(result, value...)
			} else {
				result = append(result, '?')
			}
			i = j + 1
		} else {
			result = append(result, s[i])
			i++
		}
	}
	return string(result)
}
