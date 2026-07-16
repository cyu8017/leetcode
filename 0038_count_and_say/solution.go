// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

import "strconv"

func countAndSay(n int) string {
	term := "1"

	for i := 1; i < n; i++ {
		nextTerm := make([]byte, 0, len(term)*2)
		index := 0
		for index < len(term) {
			count := 1
			for index+count < len(term) && term[index+count] == term[index] {
				count++
			}
			nextTerm = append(nextTerm, strconv.Itoa(count)...)
			nextTerm = append(nextTerm, term[index])
			index += count
		}
		term = string(nextTerm)
	}

	return term
}
