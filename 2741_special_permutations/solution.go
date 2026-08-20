// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/


func specialPerm(nums []int) int {
	const MOD = 1000000007
	n := len(nums)
	memo := make([][]int, 1<<n)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dfs func(mask, last int) int
	dfs = func(mask, last int) int {
		if mask == (1<<n)-1 {
			return 1
		}
		if memo[mask][last] != -1 {
			return memo[mask][last]
		}
		res := 0
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			if nums[i]%nums[last] == 0 || nums[last]%nums[i] == 0 {
				res = (res + dfs(mask|1<<i, i)) % MOD
			}
		}
		memo[mask][last] = res
		return res
	}
	ans := 0
	for i := 0; i < n; i++ {
		ans = (ans + dfs(1<<i, i)) % MOD
	}
	return ans
}
