// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

import "strings"

func fullJustify(words []string, maxWidth int) []string {
	result := make([]string, 0)
	i := 0

	for i < len(words) {
		lineWords := make([]string, 0)
		lineLen := 0

		for i < len(words) {
			word := words[i]
			extra := 0
			if len(lineWords) > 0 {
				extra = 1
			}
			if lineLen+len(word)+extra > maxWidth {
				break
			}
			lineWords = append(lineWords, word)
			lineLen += len(word) + extra
			i++
		}

		if i == len(words) || len(lineWords) == 1 {
			line := strings.Join(lineWords, " ")
			line += strings.Repeat(" ", maxWidth-len(line))
			result = append(result, line)
		} else {
			totalChars := 0
			for _, word := range lineWords {
				totalChars += len(word)
			}
			totalSpaces := maxWidth - totalChars
			gaps := len(lineWords) - 1
			space := totalSpaces / gaps
			remainder := totalSpaces % gaps
			var builder strings.Builder
			for j, word := range lineWords[:len(lineWords)-1] {
				builder.WriteString(word)
				gapSpaces := space
				if j < remainder {
					gapSpaces++
				}
				builder.WriteString(strings.Repeat(" ", gapSpaces))
			}
			builder.WriteString(lineWords[len(lineWords)-1])
			result = append(result, builder.String())
		}
	}

	return result
}
