// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

import "fmt"

func encodeWord(word string) string {
	size := len(word)
	best := word
	for unitLength := 1; unitLength <= size/2; unitLength++ {
		if size%unitLength != 0 {
			continue
		}
		unit := word[:unitLength]
		matches := true
		for start := unitLength; start < size; start += unitLength {
			if word[start:start+unitLength] != unit {
				matches = false
				break
			}
		}
		if !matches {
			continue
		}
		encoded := fmt.Sprintf("%d[%s]", size/unitLength, unit)
		if len(encoded) < len(best) || (len(encoded) == len(best) && encoded < best) {
			best = encoded
		}
	}
	return best
}

func encode(s string) string {
	length := len(s)
	dp := make([]string, length+1)
	for index := 1; index <= length; index++ {
		dp[index] = encodeWord(s[:index])
		for split := 1; split < index; split++ {
			candidate := dp[index-split] + encodeWord(s[index-split:index])
			if len(candidate) < len(dp[index]) || (len(candidate) == len(dp[index]) && candidate < dp[index]) {
				dp[index] = candidate
			}
		}
	}
	return dp[length]
}
