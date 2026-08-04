// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

func minRemoveToMakeValid(s string) string {
	chars := []byte(s)
	opens := []int{}
	for i, ch := range chars {
		if ch == '(' {
			opens = append(opens, i)
		} else if ch == ')' {
			if len(opens) > 0 {
				opens = opens[:len(opens)-1]
			} else {
				chars[i] = 0
			}
		}
	}
	for _, i := range opens {
		chars[i] = 0
	}
	out := make([]byte, 0, len(chars))
	for _, ch := range chars {
		if ch != 0 {
			out = append(out, ch)
		}
	}
	return string(out)
}
