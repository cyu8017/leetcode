// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

import (
	"fmt"
	"regexp"
	"strconv"
)

func solveEquation(equation string) string {
	parse := func(expr string) (int, int) {
		re := regexp.MustCompile(`[+-]?(?:\d+x|x|\d+)`)
		coef, constVal := 0, 0
		for _, token := range re.FindAllString(expr, -1) {
			if len(token) > 0 && token[len(token)-1] == 'x' {
				raw := token[:len(token)-1]
				if raw == "" || raw == "+" {
					coef++
				} else if raw == "-" {
					coef--
				} else {
					v, _ := strconv.Atoi(raw)
					coef += v
				}
			} else {
				v, _ := strconv.Atoi(token)
				constVal += v
			}
		}
		return coef, constVal
	}
	parts := splitEq(equation)
	leftCoef, leftConst := parse(parts[0])
	rightCoef, rightConst := parse(parts[1])
	coef := leftCoef - rightCoef
	constVal := rightConst - leftConst
	if coef == 0 {
		if constVal == 0 {
			return "Infinite solutions"
		}
		return "No solution"
	}
	return fmt.Sprintf("x=%d", constVal/coef)
}

func splitEq(equation string) []string {
	for i := 0; i < len(equation); i++ {
		if equation[i] == '=' {
			return []string{equation[:i], equation[i+1:]}
		}
	}
	return []string{equation, ""}
}
