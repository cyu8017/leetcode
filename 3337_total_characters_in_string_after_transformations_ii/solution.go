// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

func lengthAfterTransformations(s string, t int, nums []int) int {
	const mod = 1000000007
	mat := make([][]int, 26)
	for i := range mat {
		mat[i] = make([]int, 26)
		for j := 1; j <= nums[i]; j++ {
			mat[i][(i+j)%26] = 1
		}
	}
	mat = matPow(mat, t, mod)
	cnt := make([]int, 26)
	for _, c := range s {
		cnt[c-'a']++
	}
	ans := 0
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			ans = (ans + cnt[i]*mat[i][j]) % mod
		}
	}
	return ans
}

func matMul(a, b [][]int, mod int) [][]int {
	n := len(a)
	c := make([][]int, n)
	for i := range c {
		c[i] = make([]int, n)
		for k := 0; k < n; k++ {
			if a[i][k] == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % mod
			}
		}
	}
	return c
}

func matPow(a [][]int, e int, mod int) [][]int {
	n := len(a)
	r := make([][]int, n)
	for i := range r {
		r[i] = make([]int, n)
		r[i][i] = 1
	}
	for e > 0 {
		if e&1 == 1 {
			r = matMul(r, a, mod)
		}
		a = matMul(a, a, mod)
		e >>= 1
	}
	return r
}
