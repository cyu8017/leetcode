// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/


func isReachable(targetX int, targetY int) bool {
	g := gcd2543(targetX, targetY)
	for g%2 == 0 {
		g /= 2
	}
	return g == 1
}
func gcd2543(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
