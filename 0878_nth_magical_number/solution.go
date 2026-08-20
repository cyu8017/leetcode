// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

func nthMagicalNumber(n int, a int, b int) int {
	const MOD = 1_000_000_007
	g := a
	bb := b
	for bb != 0 {
		g, bb = bb, g%bb
	}
	lcm := a / g * b
	lo, hi := 1, n
	if a < b {
		hi *= a
	} else {
		hi *= b
	}
	for lo < hi {
		mid := (lo + hi) / 2
		if mid/a+mid/b-mid/lcm >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo % MOD
}
