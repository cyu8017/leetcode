// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

import (
	"fmt"
	"regexp"
	"strconv"
)

func fractionAddition(expression string) string {
	re := regexp.MustCompile(`[+-]?\d+`)
	parts := re.FindAllString(expression, -1)
	nums := make([]int, len(parts))
	for i, p := range parts {
		nums[i], _ = strconv.Atoi(p)
	}
	numerator, denominator := 0, 1
	for i := 0; i < len(nums); i += 2 {
		a, b := nums[i], nums[i+1]
		numerator = numerator*b + a*denominator
		denominator *= b
		g := gcdAbs(numerator, denominator)
		numerator /= g
		denominator /= g
	}
	return fmt.Sprintf("%d/%d", numerator, denominator)
}

func gcdAbs(a, b int) int {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
