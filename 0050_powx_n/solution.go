// LeetCode 0050 - Pow(x, n)
// https://leetcode.com/problems/powx-n/

func myPow(x float64, n int) float64 {
	exp := int64(n)
	if exp == 0 {
		return 1.0
	}

	if exp < 0 {
		x = 1.0 / x
		exp = -exp
	}

	result := 1.0
	current := x

	for exp != 0 {
		if exp&1 != 0 {
			result *= current
		}
		current *= current
		exp >>= 1
	}

	return result
}
