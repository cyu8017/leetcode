// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

import "strings"

func canTransform(start string, result string) bool {
	if strings.ReplaceAll(start, "X", "") != strings.ReplaceAll(result, "X", "") {
		return false
	}
	i, j, n := 0, 0, len(start)
	for i < n && j < n {
		for i < n && start[i] == 'X' {
			i++
		}
		for j < n && result[j] == 'X' {
			j++
		}
		if i == n || j == n {
			break
		}
		if start[i] != result[j] {
			return false
		}
		if start[i] == 'L' && i < j {
			return false
		}
		if start[i] == 'R' && i > j {
			return false
		}
		i++
		j++
	}
	return true
}
