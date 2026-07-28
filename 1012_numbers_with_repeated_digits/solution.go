// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

func numDupDigitsAtMostN(n int) int {
	s := []byte{}
	for x := n; x > 0; x /= 10 {
		s = append([]byte{byte(x%10) + '0'}, s...)
	}
	m := len(s)
	p := func(a, b int) int {
		res := 1
		for i := 0; i < b; i++ {
			res *= a - i
		}
		return res
	}
	totalUnique := 0
	for length := 1; length < m; length++ {
		totalUnique += 9 * p(9, length-1)
	}
	used := map[int]bool{}
	broken := false
	for i, ch := range s {
		d := int(ch - '0')
		start := 0
		if i == 0 {
			start = 1
		}
		for x := start; x < d; x++ {
			if used[x] {
				continue
			}
			totalUnique += p(9-i, m-i-1)
		}
		if used[d] {
			broken = true
			break
		}
		used[d] = true
	}
	if !broken {
		totalUnique++
	}
	return n - totalUnique
}
