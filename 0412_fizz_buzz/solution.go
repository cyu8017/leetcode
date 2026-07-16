// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

import "strconv"

func fizzBuzz(n int) []string {
	result := make([]string, 0, n)
	for value := 1; value <= n; value++ {
		switch {
		case value%15 == 0:
			result = append(result, "FizzBuzz")
		case value%3 == 0:
			result = append(result, "Fizz")
		case value%5 == 0:
			result = append(result, "Buzz")
		default:
			result = append(result, strconv.Itoa(value))
		}
	}
	return result
}
