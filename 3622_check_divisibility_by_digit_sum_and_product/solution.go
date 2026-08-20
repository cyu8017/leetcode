// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

func checkDivisibility(n int) bool {
	s, p := 0, 1
	x := n
	for x != 0 {
		v := x % 10
		x /= 10
		s += v
		p *= v
	}
	return n%(s+p) == 0
}
