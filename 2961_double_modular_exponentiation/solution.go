// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

func getGoodIndices(variables [][]int, target int) []int {
	modPow := func(a, b, mod int) int {
		res := 1 % mod
		a %= mod
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	ans := []int{}
	for i, v := range variables {
		a, b, c, m := v[0], v[1], v[2], v[3]
		if modPow(modPow(a, b, 10), c, m) == target {
			ans = append(ans, i)
		}
	}
	return ans
}
