// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

func isArmstrong(n int) bool {
	digits := 0
	for x := n; x > 0; x /= 10 {
		digits++
	}
	sum := 0
	for x := n; x > 0; x /= 10 {
		d := x % 10
		p := 1
		for i := 0; i < digits; i++ {
			p *= d
		}
		sum += p
	}
	return sum == n
}
