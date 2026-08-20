// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

func countSubMultisets(nums []int, l int, r int) int {
	const mod = 1_000_000_007
	freq := map[int]int{}
	total := 0
	for _, v := range nums {
		freq[v]++
		total += v
	}
	if total < l {
		return 0
	}
	if r > total {
		r = total
	}
	dp := make([]int, r+1)
	dp[0] = 1
	zeros := freq[0]
	delete(freq, 0)
	for v, c := range freq {
		ndp := make([]int, r+1)
		for sum := 0; sum <= r; sum++ {
			if dp[sum] == 0 {
				continue
			}
			for k := 0; k <= c && sum+k*v <= r; k++ {
				ndp[sum+k*v] = (ndp[sum+k*v] + dp[sum]) % mod
			}
		}
		dp = ndp
	}
	ans := 0
	for s := l; s <= r; s++ {
		ans = (ans + dp[s]) % mod
	}
	ans = ans * (zeros + 1) % mod
	return ans
}
