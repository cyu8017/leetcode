// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

func concatenatedBinary(n int) int {
	ans, bits, mod := 0, 0, 1000000007
	for x := 1; x <= n; x++ {
		if x&(x-1) == 0 {
			bits++
		}
		ans = ((ans<<bits)%mod + x) % mod
	}
	return ans
}
