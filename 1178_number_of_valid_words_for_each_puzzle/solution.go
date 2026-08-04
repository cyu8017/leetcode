// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

func findNumOfValidWords(words []string, puzzles []string) []int {
	maskOf := func(s string) int {
		mask := 0
		for i := 0; i < len(s); i++ {
			mask |= 1 << (s[i] - 'a')
		}
		return mask
	}
	freq := map[int]int{}
	for _, w := range words {
		freq[maskOf(w)]++
	}
	ans := make([]int, len(puzzles))
	for i, puzzle := range puzzles {
		first := 1 << (puzzle[0] - 'a')
		full := maskOf(puzzle)
		sub := full
		total := 0
		for {
			if sub&first != 0 {
				total += freq[sub]
			}
			if sub == 0 {
				break
			}
			sub = (sub - 1) & full
		}
		ans[i] = total
	}
	return ans
}
