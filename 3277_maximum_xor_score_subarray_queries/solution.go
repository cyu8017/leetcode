// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

func maximumSubarrayXor(nums []int, queries [][]int) []int {
	n := len(nums)
	// xorScore of subarray can be computed via DP
	// f[i][j] = xor score of nums[i..j]
	f := make([][]int, n)
	for i := range f {
		f[i] = make([]int, n)
		f[i][i] = nums[i]
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			f[i][j] = f[i][j-1] ^ f[i+1][j]
		}
	}
	best := make([][]int, n)
	for i := range best {
		best[i] = make([]int, n)
		best[i][i] = f[i][i]
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			best[i][j] = f[i][j]
			if best[i][j-1] > best[i][j] {
				best[i][j] = best[i][j-1]
			}
			if best[i+1][j] > best[i][j] {
				best[i][j] = best[i+1][j]
			}
		}
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		ans[i] = best[q[0]][q[1]]
	}
	return ans
}
