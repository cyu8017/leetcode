// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

func numSteps(s string) int {
	steps, carry := 0, 0
	for i := len(s) - 1; i >= 1; i-- {
		value := int(s[i]-'0') + carry
		if value == 1 {
			steps += 2
			carry = 1
		} else {
			steps++
		}
	}
	return steps + carry
}
