// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

func maxSideLength(mat [][]int, threshold int) int {
	m, n := len(mat), len(mat[0])
	prefix := make([][]int, m+1)
	for i := range prefix {
		prefix[i] = make([]int, n+1)
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			prefix[r+1][c+1] = mat[r][c] + prefix[r][c+1] + prefix[r+1][c] - prefix[r][c]
		}
	}
	possible := func(size int) bool {
		for r := size; r <= m; r++ {
			for c := size; c <= n; c++ {
				sum := prefix[r][c] - prefix[r-size][c] - prefix[r][c-size] + prefix[r-size][c-size]
				if sum <= threshold {
					return true
				}
			}
		}
		return false
	}
	lo, hi := 0, m
	if n < hi {
		hi = n
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if possible(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
