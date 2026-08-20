// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

func minSteps(n int) int {
	steps := 0
	factor := 2
	for factor*factor <= n {
		for n%factor == 0 {
			steps += factor
			n /= factor
		}
		factor++
	}
	if n > 1 {
		steps += n
	}
	return steps
}
