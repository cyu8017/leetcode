// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

import (
	"strconv"
	"unicode"
)

func diffWaysToCompute(expression string) []int {
	if isDigitsOnly(expression) {
		value, _ := strconv.Atoi(expression)
		return []int{value}
	}
	result := []int{}
	for index, operator := range expression {
		if operator != '+' && operator != '-' && operator != '*' {
			continue
		}
		left := diffWaysToCompute(expression[:index])
		right := diffWaysToCompute(expression[index+1:])
		for _, leftValue := range left {
			for _, rightValue := range right {
				switch operator {
				case '+':
					result = append(result, leftValue+rightValue)
				case '-':
					result = append(result, leftValue-rightValue)
				default:
					result = append(result, leftValue*rightValue)
				}
			}
		}
	}
	return result
}

func isDigitsOnly(expression string) bool {
	for _, char := range expression {
		if !unicode.IsDigit(char) {
			return false
		}
	}
	return true
}
