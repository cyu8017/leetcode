// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/


func minOperations(n int) int {
	ans := 0
	for n > 0 {
		if n&3 == 3 {
			n++
			ans++
		} else if n&1 == 1 {
			n--
			ans++
		} else {
			n >>= 1
		}
	}
	return ans
}
