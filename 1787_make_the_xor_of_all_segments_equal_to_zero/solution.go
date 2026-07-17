// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

func minChanges(nums []int, k int) int {
	freq := make([][]int, k)
	for i := range freq {
		freq[i] = make([]int, 1024)
	}
	size := make([]int, k)
	for i, x := range nums {
		freq[i%k][x]++
		size[i%k]++
	}
	const inf = 1000000000
	dp := make([]int, 256)
	for j := range dp {
		dp[j] = inf
	}
	dp[0] = 0
	for i := 0; i < k; i++ {
		ndp := make([]int, 256)
		for j := range ndp {
			ndp[j] = inf
		}
		for xv := 0; xv < 256; xv++ {
			cost := size[i] - freq[i][xv]
			for xo := 0; xo < 256; xo++ {
				if dp[xo] == inf {
					continue
				}
				key := xo ^ xv
				if dp[xo]+cost < ndp[key] {
					ndp[key] = dp[xo] + cost
				}
			}
		}
		dp = ndp
	}
	return dp[0]
}
