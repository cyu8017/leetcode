// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

func smallestNumber(num string, t int64) string {
	// factor t into digits 9..2
	need := map[int]int{}
	tt := t
	for d := 9; d >= 2; d-- {
		for tt%d == 0 {
			need[d]++
			tt /= int64(d)
		}
	}
	if tt > 1 {
		return "-1"
	}
	// build smallest number >= num with digit product divisible by t
	// Try same length first then longer
	for extra := 0; extra <= 60; extra++ {
		L := len(num) + extra
		res := make([]byte, L)
		if dfs3348(res, 0, true, extra == 0, num, t) {
			return string(res)
		}
	}
	return "-1"
}

func dfs3348(res []byte, i int, tight bool, sameLen bool, num string, t int64) bool {
	if i == len(res) {
		prod := int64(1)
		for _, c := range res {
			prod *= int64(c - '0')
			if prod == 0 {
				break
			}
		}
		return prod%t == 0 && prod > 0
	}
	start := byte('0')
	if i == 0 {
		start = '1'
	}
	if tight && sameLen && i < len(num) {
		start = num[i]
	}
	for c := start; c <= '9'; c++ {
		res[i] = c
		nt := tight && sameLen && i < len(num) && c == num[i]
		if dfs3348(res, i+1, nt, sameLen, num, t) {
			return true
		}
	}
	return false
}
