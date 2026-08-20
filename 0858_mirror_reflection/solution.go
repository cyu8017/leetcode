// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

func mirrorReflection(p int, q int) int {
	g := gcd(p, q)
	p /= g
	q /= g
	if p%2 == 0 {
		return 2
	}
	if q%2 == 0 {
		return 0
	}
	return 1
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
