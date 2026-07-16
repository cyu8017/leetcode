// LeetCode 0357 - Count Numbers with Unique Digits
// https://leetcode.com/problems/count-numbers-with-unique-digits/

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}

	total := 10
	unique := 9
	available := 9

	for length := 2; length <= n; length++ {
		unique *= available
		available--
		total += unique
	}

	return total
}
