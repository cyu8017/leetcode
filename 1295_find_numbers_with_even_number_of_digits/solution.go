// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

func findNumbers(nums []int) int {
	ans := 0
	for _, value := range nums {
		digits := 0
		for value > 0 {
			value /= 10
			digits++
		}
		if digits%2 == 0 {
			ans++
		}
	}
	return ans
}
