// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

func superPow(a int, b []int) int {
	const mod = 1337
	a %= mod
	result := 1

	powMod := func(base int, exponent int) int {
		value := 1
		current := base
		for exponent > 0 {
			if exponent&1 == 1 {
				value = value * current % mod
			}
			current = current * current % mod
			exponent >>= 1
		}
		return value
	}

	for _, digit := range b {
		result = powMod(result, 10) * powMod(a, digit) % mod
	}

	return result
}
