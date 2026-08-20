// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

import "strings"

func isValid(code string) bool {
	stack := []string{}
	i := 0
	n := len(code)
	for i < n {
		if strings.HasPrefix(code[i:], "<![CDATA[") {
			if len(stack) == 0 {
				return false
			}
			j := strings.Index(code[i+9:], "]]>")
			if j < 0 {
				return false
			}
			i = i + 9 + j + 3
		} else if strings.HasPrefix(code[i:], "</") {
			j := strings.Index(code[i+2:], ">")
			if j < 0 {
				return false
			}
			tag := code[i+2 : i+2+j]
			if len(stack) == 0 || stack[len(stack)-1] != tag {
				return false
			}
			stack = stack[:len(stack)-1]
			i = i + 2 + j + 1
			if len(stack) == 0 && i < n {
				return false
			}
		} else if code[i] == '<' {
			j := strings.Index(code[i+1:], ">")
			if j < 0 {
				return false
			}
			tag := code[i+1 : i+1+j]
			if len(tag) == 0 || len(tag) > 9 {
				return false
			}
			for _, ch := range tag {
				if ch < 'A' || ch > 'Z' {
					return false
				}
			}
			stack = append(stack, tag)
			i = i + 1 + j + 1
		} else {
			if len(stack) == 0 {
				return false
			}
			i++
		}
	}
	return len(stack) == 0
}
