// LeetCode 2119 - A Number After a Double Reversal
// https://leetcode.com/problems/a-number-after-a-double-reversal/

func isSameAfterReversals(num int) bool {
	return num == 0 || num%10 != 0
}
