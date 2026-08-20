// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

func minimizeSet(divisor1 int, divisor2 int, uniqueCnt1 int, uniqueCnt2 int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	lcm := divisor1 / gcd(divisor1, divisor2) * divisor2
	ok := func(x int) bool {
		a := x - x/divisor1
		b := x - x/divisor2
		both := x - x/lcm
		return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1+uniqueCnt2
	}
	lo, hi := 1, 1<<62
	for lo < hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
