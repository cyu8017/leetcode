// LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

func distanceSum(m int, n int, k int) int {
	const mod = 1000000007
	// sum over all pairs of cells of dist * C(mn-2, k-2)
	if k < 2 {
		return 0
	}
	totalCells := m * n
	pairChoose := comb3426(totalCells-2, k-2, mod)
	var sumDist int64
	// sum of |r1-r2| over all cell pairs
	for d := 1; d < m; d++ {
		sumDist += int64(d) * int64(m-d) * int64(n) * int64(n)
	}
	for d := 1; d < n; d++ {
		sumDist += int64(d) * int64(n-d) * int64(m) * int64(m)
	}
	return int(sumDist % mod * int64(pairChoose) % mod)
}

func comb3426(n, k, mod int) int {
	if k < 0 || k > n {
		return 0
	}
	num, den := 1, 1
	for i := 0; i < k; i++ {
		num = int(int64(num) * int64(n-i) % int64(mod))
		den = int(int64(den) * int64(i+1) % int64(mod))
	}
	return int(int64(num) * modPow3426(den, mod-2, mod) % int64(mod))
}
func modPow3426(a, e, mod int) int {
	r := 1
	for e > 0 {
		if e&1 == 1 {
			r = int(int64(r) * int64(a) % int64(mod))
		}
		a = int(int64(a) * int64(a) % int64(mod))
		e >>= 1
	}
	return r
}
