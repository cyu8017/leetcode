// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/


import "sort"

func splitNum(num int) int {
	digits := []int{}
	for num > 0 {
		digits = append(digits, num%10)
		num /= 10
	}
	sort.Ints(digits)
	a, b := 0, 0
	for i, d := range digits {
		if i%2 == 0 {
			a = a*10 + d
		} else {
			b = b*10 + d
		}
	}
	return a + b
}
