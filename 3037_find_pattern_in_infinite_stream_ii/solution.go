// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

/**
 * Definition for an infinite stream.
 * type InfiniteStream interface {
 *     Next() int
 * }
 */
func findPattern(stream InfiniteStream, pattern []int) int {
	lps := getLPS(pattern)
	i, j := 0, 0
	bit := 0
	readNext := false
	for {
		if !readNext {
			bit = stream.Next()
			readNext = true
		}
		if bit == pattern[j] {
			i++
			readNext = false
			j++
			if j == len(pattern) {
				return i - j
			}
		} else if j > 0 {
			j = lps[j-1]
		} else {
			i++
			readNext = false
		}
	}
}

func getLPS(pattern []int) []int {
	lps := make([]int, len(pattern))
	j := 0
	for i := 1; i < len(pattern); i++ {
		for j > 0 && pattern[j] != pattern[i] {
			j = lps[j-1]
		}
		if pattern[i] == pattern[j] {
			j++
			lps[i] = j
		}
	}
	return lps
}
