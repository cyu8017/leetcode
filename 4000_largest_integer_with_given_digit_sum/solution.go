// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

func largestInteger(n int, s int) (ans int) {
	if n*9 < s {
		return -1
	}
	for i := 0; i < n; i++ {
		x := min(s, 9)
		ans = ans*10 + x
		s -= x
	}
	return
}
