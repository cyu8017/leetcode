// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

func nthUglyNumber(n int, a int, b int, c int) int {
	gcd := func(x, y int) int {
		for y != 0 {
			x, y = y, x%y
		}
		return x
	}
	lcm := func(x, y int) int { return x / gcd(x, y) * y }
	ab, ac, bc := lcm(a, b), lcm(a, c), lcm(b, c)
	abc := lcm(ab, c)
	count := func(x int) int {
		return x/a + x/b + x/c - x/ab - x/ac - x/bc + x/abc
	}
	lo, hi := 1, 2000000000
	for lo < hi {
		mid := lo + (hi-lo)/2
		if count(mid) >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
