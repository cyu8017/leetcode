// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

import "sort"

func smallestNumber(num int64) int64 {
	neg := num < 0
	if neg {
		num = -num
	}
	digits := []byte{}
	if num == 0 {
		return 0
	}
	for num > 0 {
		digits = append(digits, byte('0'+num%10))
		num /= 10
	}
	if neg {
		sort.Slice(digits, func(i, j int) bool { return digits[i] > digits[j] })
		var ans int64
		for _, d := range digits {
			ans = ans*10 + int64(d-'0')
		}
		return -ans
	}
	sort.Slice(digits, func(i, j int) bool { return digits[i] < digits[j] })
	if digits[0] == '0' {
		for i := 1; i < len(digits); i++ {
			if digits[i] != '0' {
				digits[0], digits[i] = digits[i], digits[0]
				break
			}
		}
	}
	var ans int64
	for _, d := range digits {
		ans = ans*10 + int64(d-'0')
	}
	return ans
}
