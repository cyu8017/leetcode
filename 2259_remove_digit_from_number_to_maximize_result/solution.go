// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

func removeDigit(number string, digit byte) string {
	best := ""
	for i := 0; i < len(number); i++ {
		if number[i] == digit {
			cand := number[:i] + number[i+1:]
			if cand > best {
				best = cand
			}
		}
	}
	return best
}
