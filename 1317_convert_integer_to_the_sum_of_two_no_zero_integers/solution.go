// LeetCode 1317 - Convert Integer to the Sum of Two No-Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

func getNoZeroIntegers(n int) []int {
	valid := func(value int) bool {
		for value > 0 {
			if value%10 == 0 {
				return false
			}
			value /= 10
		}
		return true
	}
	for first := 1; first < n; first++ {
		if valid(first) && valid(n-first) {
			return []int{first, n - first}
		}
	}
	return nil
}
