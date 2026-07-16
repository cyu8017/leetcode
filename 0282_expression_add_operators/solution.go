// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

import "strconv"

func addOperators(num string, target int) []string {
	result := make([]string, 0)

	var backtrack func(index int, path string, value int64, previous int64)
	backtrack = func(index int, path string, value int64, previous int64) {
		if index == len(num) {
			if value == int64(target) {
				result = append(result, path)
			}
			return
		}
		for end := index; end < len(num); end++ {
			if end > index && num[index] == '0' {
				break
			}
			currentStr := num[index : end+1]
			current, _ := strconv.ParseInt(currentStr, 10, 64)
			if index == 0 {
				backtrack(end+1, currentStr, current, current)
			} else {
				backtrack(end+1, path+"+"+currentStr, value+current, current)
				backtrack(end+1, path+"-"+currentStr, value-current, -current)
				backtrack(end+1, path+"*"+currentStr, value-previous+previous*current, previous*current)
			}
		}
	}

	backtrack(0, "", 0, 0)
	return result
}
