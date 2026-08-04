// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

func minOperations(nums []int) int {
	adds, maxBits := 0, 0
	for _, x := range nums {
		bits := 0
		for t := x; t > 0; t >>= 1 {
			adds += t & 1
			bits++
		}
		if bits-1 > maxBits {
			maxBits = bits - 1
		}
	}
	return adds + maxBits
}
