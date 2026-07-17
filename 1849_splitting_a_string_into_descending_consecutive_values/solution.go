// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

import "strconv"

func splitString(s string) bool {
	return dfsSplitString(s, 0, nil, 0)
}

func dfsSplitString(s string, index int, previous *int, parts int) bool {
	if index == len(s) {
		return parts >= 2
	}

	for end := index + 1; end <= len(s); end++ {
		value, err := strconv.Atoi(s[index:end])
		if err != nil {
			continue
		}

		if previous == nil {
			if dfsSplitString(s, end, &value, parts+1) {
				return true
			}
			continue
		}

		if value == *previous-1 {
			if dfsSplitString(s, end, &value, parts+1) {
				return true
			}
		} else if value > *previous-1 {
			break
		}
	}

	return false
}
