// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/


func makeTheIntegerZero(num1 int, num2 int) int {
	for ops := 1; ops <= 60; ops++ {
		remain := int64(num1) - int64(ops)*int64(num2)
		if remain < int64(ops) {
			continue
		}
		bits := bitsCount2749(remain)
		if bits <= ops {
			return ops
		}
	}
	return -1
}
func bitsCount2749(x int64) int {
	cnt := 0
	for x > 0 {
		cnt++
		x &= x - 1
	}
	return cnt
}
