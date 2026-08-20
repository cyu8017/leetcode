// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

func replaceNonCoprimes(nums []int) []int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	stack := []int{}
	for _, x := range nums {
		for len(stack) > 0 {
			g := gcd(stack[len(stack)-1], x)
			if g == 1 {
				break
			}
			x = stack[len(stack)-1] / g * x
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, x)
	}
	return stack
}
