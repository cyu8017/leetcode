// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

func lastRemaining(n int64) int64 {
	first, step, left := int64(1), int64(2), true
	for n > 1 {
		if !left && n%2 == 0 {
			first += step
		}
		n = (n + 1) / 2
		step *= 2
		left = !left
	}
	return first
}