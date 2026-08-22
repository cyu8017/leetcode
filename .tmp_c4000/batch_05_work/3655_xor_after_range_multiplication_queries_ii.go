// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

func xorAfterQueries(nums []int, queries [][]int) int {
	const MOD = 1_000_000_007
	n := len(nums)
	// Difference array per step for large updates; apply then xor
	diff := make([]int, n+1)
	for i := range diff {
		diff[i] = 1
	}
	type upd struct{ l, r, k, v int }
	// For each unique k, apply range multiplies on arithmetic progression
	byK := map[int][]upd{}
	for _, q := range queries {
		l, r, k, v := q[0], q[1], q[2], q[3]
		byK[k] = append(byK[k], upd{l, r, k, v})
	}
	res := append([]int(nil), nums...)
	for k, ups := range byK {
		fac := make([]int, n)
		for i := range fac {
			fac[i] = 1
		}
		for _, u := range ups {
			for i := u.l; i <= u.r; i += k {
				fac[i] = fac[i] * u.v % MOD
			}
		}
		for i := 0; i < n; i++ {
			res[i] = res[i] * fac[i] % MOD
		}
	}
	ans := 0
	for _, v := range res {
		ans ^= v
	}
	return ans
}
