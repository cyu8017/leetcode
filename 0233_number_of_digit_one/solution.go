// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

func countDigitOne(n int) int {
	count := 0
	factor := 1
	for factor <= n {
		lower := n % factor
		current := (n / factor) % 10
		higher := n / (factor * 10)
		switch {
		case current == 0:
			count += higher * factor
		case current == 1:
			count += higher*factor + lower + 1
		default:
			count += (higher + 1) * factor
		}
		factor *= 10
	}
	return count
}
