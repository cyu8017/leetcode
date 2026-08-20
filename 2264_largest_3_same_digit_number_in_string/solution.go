// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

func largestGoodInteger(num string) string {
	best := ""
	for i := 0; i+2 < len(num); i++ {
		if num[i] == num[i+1] && num[i] == num[i+2] {
			cand := num[i : i+3]
			if cand > best {
				best = cand
			}
		}
	}
	return best
}
