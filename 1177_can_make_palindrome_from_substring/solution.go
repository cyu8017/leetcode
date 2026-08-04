// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

func canMakePaliQueries(s string, queries [][]int) []bool {
	prefix := make([]int, len(s)+1)
	mask := 0
	for i := 0; i < len(s); i++ {
		mask ^= 1 << (s[i] - 'a')
		prefix[i+1] = mask
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		bits := bitsCount(prefix[q[1]+1] ^ prefix[q[0]])
		ans[i] = bits/2 <= q[2]
	}
	return ans
}

func bitsCount(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
