// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/


func monkeyMove(n int) int {
	const MOD = 1000000007
	pow := func(a, e int) int {
		res := 1
		for e > 0 {
			if e&1 == 1 {
				res = res * a % MOD
			}
			a = a * a % MOD
			e >>= 1
		}
		return res
	}
	return (pow(2, n) - 2 + MOD) % MOD
}
