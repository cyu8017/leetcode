// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

func maxSum(nums []int, k int) int {
	const mod = 1_000_000_007
	cnt := make([]int, 32)
	for _, v := range nums {
		for b := 0; b < 32; b++ {
			if v&(1<<b) != 0 {
				cnt[b]++
			}
		}
	}
	ans := 0
	for i := 0; i < k; i++ {
		cur := 0
		for b := 0; b < 32; b++ {
			if cnt[b] > 0 {
				cur |= 1 << b
				cnt[b]--
			}
		}
		ans = (ans + cur%mod*cur%mod) % mod
	}
	return ans
}
