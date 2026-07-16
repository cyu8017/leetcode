// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

import (
	"strconv"
	"strings"
)

func isAdditiveNumber(num string) bool {
	valid := func(first, second string, start int) bool {
		if (len(first) > 1 && first[0] == '0') || (len(second) > 1 && second[0] == '0') {
			return false
		}
		for start < len(num) {
			firstValue, _ := strconv.ParseInt(first, 10, 64)
			secondValue, _ := strconv.ParseInt(second, 10, 64)
			total := strconv.FormatInt(firstValue+secondValue, 10)
			if !strings.HasPrefix(num[start:], total) {
				return false
			}
			first = second
			second = total
			start += len(total)
		}
		return true
	}

	for firstEnd := 1; firstEnd < len(num); firstEnd++ {
		for secondEnd := firstEnd + 1; secondEnd < len(num); secondEnd++ {
			if valid(num[:firstEnd], num[firstEnd:secondEnd], secondEnd) {
				return true
			}
		}
	}
	return false
}
