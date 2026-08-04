// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

import "fmt"

func simplifiedFractions(n int) []string {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	var answer []string
	for a := 1; a < n; a++ {
		for b := a + 1; b <= n; b++ {
			if gcd(a, b) == 1 {
				answer = append(answer, fmt.Sprintf("%d/%d", a, b))
			}
		}
	}
	return answer
}
