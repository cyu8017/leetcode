// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

func findIntegers(n int) int {
	fib := make([]int, 32)
	fib[0], fib[1] = 1, 2
	for i := 2; i < 32; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}
	answer := 0
	prevBit := 0
	for bit := 30; bit >= 0; bit-- {
		if n&(1<<bit) != 0 {
			answer += fib[bit]
			if prevBit == 1 {
				return answer
			}
			prevBit = 1
		} else {
			prevBit = 0
		}
	}
	return answer + 1
}
