// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

func minOperations(queries [][]int) int64 {
	var ans int64
	opsToZero := func(x int) int {
		// times floor_div_4 until 0
		ops := 0
		for x > 0 {
			x /= 4
			ops++
		}
		return ops
	}
	// prefix of ops for numbers 1..n
	// For range [l,r], sum of ops for each number, answer ceil(sum/2)
	for _, q := range queries {
		l, r := q[0], q[1]
		var sum int64
		for x := l; x <= r; x++ {
			sum += int64(opsToZero(x))
		}
		ans += (sum + 1) / 2
	}
	return ans
}
