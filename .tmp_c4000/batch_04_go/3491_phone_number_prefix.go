// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

import "sort"

func phonePrefix(numbers []string) bool {
	sort.Strings(numbers)
	for i := 0; i+1 < len(numbers); i++ {
		if len(numbers[i]) <= len(numbers[i+1]) && numbers[i+1][:len(numbers[i])] == numbers[i] {
			return false
		}
	}
	return true
}
