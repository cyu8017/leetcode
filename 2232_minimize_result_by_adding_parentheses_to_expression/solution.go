// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

import "strconv"

func minimizeResult(expression string) string {
	plus := 0
	for i := 0; i < len(expression); i++ {
		if expression[i] == '+' {
			plus = i
			break
		}
	}
	left, right := expression[:plus], expression[plus+1:]
	bestVal := int(^uint(0) >> 1)
	best := ""
	for i := 0; i < len(left); i++ {
		for j := 1; j <= len(right); j++ {
			a, b, c, d := left[:i], left[i:], right[:j], right[j:]
			bi, _ := strconv.Atoi(b)
			ci, _ := strconv.Atoi(c)
			val := bi + ci
			if a != "" {
				ai, _ := strconv.Atoi(a)
				val *= ai
			}
			if d != "" {
				di, _ := strconv.Atoi(d)
				val *= di
			}
			cand := a + "(" + b + "+" + c + ")" + d
			if val < bestVal {
				bestVal = val
				best = cand
			}
		}
	}
	return best
}
