// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

func isSolvable(words []string, result string) bool {
	maxWord := 0
	for _, w := range words {
		if len(w) > maxWord {
			maxWord = len(w)
		}
	}
	if maxWord > len(result) {
		return false
	}
	letters := map[byte]bool{}
	for _, w := range words {
		for i := 0; i < len(w); i++ {
			letters[w[i]] = true
		}
	}
	for i := 0; i < len(result); i++ {
		letters[result[i]] = true
	}
	if len(letters) > 10 {
		return false
	}
	leading := map[byte]bool{}
	for _, w := range words {
		if len(w) > 1 {
			leading[w[0]] = true
		}
	}
	if len(result) > 1 {
		leading[result[0]] = true
	}
	value := map[byte]int{}
	used := make([]bool, 10)
	width := len(result)

	var solve func(column, row, total int) bool
	solve = func(column, row, total int) bool {
		if column == width {
			return total == 0
		}
		if row < len(words) {
			if column >= len(words[row]) {
				return solve(column, row+1, total)
			}
			ch := words[row][len(words[row])-1-column]
			if v, ok := value[ch]; ok {
				return solve(column, row+1, total+v)
			}
			for digit := 0; digit < 10; digit++ {
				if !used[digit] && (digit != 0 || !leading[ch]) {
					value[ch] = digit
					used[digit] = true
					if solve(column, row+1, total+digit) {
						return true
					}
					used[digit] = false
					delete(value, ch)
				}
			}
			return false
		}
		chR := result[len(result)-1-column]
		digitR, carry := total%10, total/10
		if v, ok := value[chR]; ok {
			return v == digitR && solve(column+1, 0, carry)
		}
		if used[digitR] || (digitR == 0 && leading[chR]) {
			return false
		}
		value[chR] = digitR
		used[digitR] = true
		ok := solve(column+1, 0, carry)
		used[digitR] = false
		delete(value, chR)
		return ok
	}
	return solve(0, 0, 0)
}
