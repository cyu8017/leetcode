// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

func canMeasureWater(x int, y int, target int) bool {
	if target == 0 {
		return true
	}
	if x+y < target {
		return false
	}
	return target%gcd(x, y) == 0
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
