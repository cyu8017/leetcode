// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

func zigZagArrays(n int, l int, r int) int {
	const mod int64 = 1000000007
	points := n + 1
	values := make([]int64, points+1)
	for m := 1; m <= points; m++ {
		up, down := make([]int64, m), make([]int64, m)
		for value := 0; value < m; value++ {
			up[value] = int64(value)
			down[value] = int64(m - 1 - value)
		}
		for length := 3; length <= n; length++ {
			nextUp, nextDown := make([]int64, m), make([]int64, m)
			prefix := int64(0)
			for value := 0; value < m; value++ {
				nextUp[value] = prefix
				prefix = (prefix + down[value]) % mod
			}
			suffix := int64(0)
			for value := m - 1; value >= 0; value-- {
				nextDown[value] = suffix
				suffix = (suffix + up[value]) % mod
			}
			up, down = nextUp, nextDown
		}
		for value := 0; value < m; value++ {
			values[m] = (values[m] + up[value] + down[value]) % mod
		}
	}
	x := int64(r-l+1) % mod
	if r-l+1 <= points {
		return int(values[r-l+1])
	}
	prefix, suffix := make([]int64, points+2), make([]int64, points+2)
	prefix[0] = 1
	for i := 1; i <= points; i++ {
		prefix[i] = prefix[i-1] * ((x - int64(i) + mod) % mod) % mod
	}
	suffix[points+1] = 1
	for i := points; i >= 1; i-- {
		suffix[i] = suffix[i+1] * ((x - int64(i) + mod) % mod) % mod
	}
	factorial := make([]int64, points+1)
	factorial[0] = 1
	for i := 1; i <= points; i++ {
		factorial[i] = factorial[i-1] * int64(i) % mod
	}
	pow := func(a, e int64) int64 {
		res := int64(1)
		for e > 0 {
			if e&1 != 0 {
				res = res * a % mod
			}
			a = a * a % mod
			e >>= 1
		}
		return res
	}
	answer := int64(0)
	for i := 1; i <= points; i++ {
		numerator := prefix[i-1] * suffix[i+1] % mod
		denominator := factorial[i-1] * factorial[points-i] % mod
		term := values[i] * numerator % mod * pow(denominator, mod-2) % mod
		if (points-i)%2 == 1 {
			answer -= term
		} else {
			answer += term
		}
		answer %= mod
	}
	if answer < 0 {
		answer += mod
	}
	return int(answer)
}