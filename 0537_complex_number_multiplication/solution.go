// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

import (
	"fmt"
	"strconv"
	"strings"
)

func complexNumberMultiply(num1 string, num2 string) string {
	parse := func(num string) (int, int) {
		parts := strings.Split(num, "+")
		real, _ := strconv.Atoi(parts[0])
		imag, _ := strconv.Atoi(strings.TrimSuffix(parts[1], "i"))
		return real, imag
	}

	a, b := parse(num1)
	c, d := parse(num2)
	real := a*c - b*d
	imag := a*d + b*c
	return fmt.Sprintf("%d+%di", real, imag)
}
