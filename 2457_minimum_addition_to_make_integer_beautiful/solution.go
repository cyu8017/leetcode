// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

func makeIntegerBeautiful(n int64, target int) int64 {
	digitSum := func(x int64) int {
		s := 0
		for x > 0 {
			s += int(x % 10)
			x /= 10
		}
		return s
	}
	orig := n
	pow := int64(1)
	for digitSum(n) > target {
		n = n/10 + 1
		pow *= 10
	}
	return n*pow - orig
}
