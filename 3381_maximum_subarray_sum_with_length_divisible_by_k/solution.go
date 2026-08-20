// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

func maxSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	pref := make([]int64, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + int64(x)
	}
	best := make([]int64, k)
	for i := range best {
		best[i] = 1 << 62
	}
	best[0] = 0
	ans := int64(-1 << 62)
	for i := 1; i <= n; i++ {
		r := i % k
		if best[r] != 1<<62 {
			cand := pref[i] - best[r]
			if cand > ans {
				ans = cand
			}
		}
		if pref[i] < best[r] {
			best[r] = pref[i]
		}
	}
	return ans
}
