// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

import "strconv"

func generateAbbreviations(word string) []string {
	result := make([]string, 0)

	var backtrack func(index int, path string, count int)
	backtrack = func(index int, path string, count int) {
		if index == len(word) {
			if count > 0 {
				result = append(result, path+strconv.Itoa(count))
			} else {
				result = append(result, path)
			}
			return
		}
		backtrack(index+1, path, count+1)
		nextPath := path
		if count > 0 {
			nextPath += strconv.Itoa(count)
		}
		nextPath += string(word[index])
		backtrack(index+1, nextPath, 0)
	}

	backtrack(0, "", 0)
	return result
}
