// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

func splitLoopedString(strs []string) string {
	bestForms := make([]string, len(strs))
	for i, s := range strs {
		rev := reverseString(s)
		if s > rev {
			bestForms[i] = s
		} else {
			bestForms[i] = rev
		}
	}
	answer := ""
	for i, original := range strs {
		var midParts []string
		midParts = append(midParts, bestForms[i+1:]...)
		midParts = append(midParts, bestForms[:i]...)
		mid := ""
		for _, part := range midParts {
			mid += part
		}
		candidates := []string{original, reverseString(original)}
		for _, candidate := range candidates {
			for cut := 0; cut < len(candidate); cut++ {
				formed := candidate[cut:] + mid + candidate[:cut]
				if formed > answer {
					answer = formed
				}
			}
		}
	}
	return answer
}

func reverseString(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
