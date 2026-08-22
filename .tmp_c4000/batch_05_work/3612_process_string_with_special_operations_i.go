// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

func processStr(s string) string {
	var result []rune
	for _, c := range s {
		if unicode.IsLetter(c) {
			result = append(result, c)
		} else if c == '*' {
			if len(result) > 0 {
				result = result[:len(result)-1]
			}
		} else if c == '#' {
			result = append(result, result...)
		} else if c == '%' {
			slices.Reverse(result)
		}
	}
	return string(result)
}
