// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/


func squareFreeSubsets(nums []int) int {
	const MOD = 1000000007
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
	maskOf := func(x int) int {
		mask := 0
		for i, p := range primes {
			cnt := 0
			for x%p == 0 {
				x /= p
				cnt++
				if cnt > 1 {
					return -1
				}
			}
			if cnt == 1 {
				mask |= 1 << i
			}
		}
		return mask
	}
	freq := map[int]int{}
	for _, x := range nums {
		freq[x]++
	}
	dp := make([]int, 1<<10)
	dp[0] = 1
	for x, c := range freq {
		if x == 1 {
			continue
		}
		m := maskOf(x)
		if m < 0 {
			continue
		}
		for state := (1 << 10) - 1; state >= 0; state-- {
			if state&m == 0 {
				dp[state|m] = (dp[state|m] + dp[state]*c) % MOD
			}
		}
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	// multiply subsets of ones: each 1 can be chosen or not -> 2^freq[1]
	ones := freq[1]
	mul := 1
	for i := 0; i < ones; i++ {
		mul = mul * 2 % MOD
	}
	ans = ans * mul % MOD
	ans = (ans - 1 + MOD) % MOD
	return ans
}
