// LeetCode 1362 - Closest Divisors
// https://leetcode.com/problems/closest-divisors/

func closestDivisors(num int) []int {
	isqrt := func(x int) int {
		r := 0
		for r*r <= x {
			r++
		}
		return r - 1
	}
	var best []int
	for _, x := range []int{num + 1, num + 2} {
		for a := isqrt(x); a >= 1; a-- {
			if x%a == 0 {
				pair := []int{a, x / a}
				if best == nil || pair[1]-pair[0] < best[1]-best[0] {
					best = pair
				}
				break
			}
		}
	}
	return best
}
