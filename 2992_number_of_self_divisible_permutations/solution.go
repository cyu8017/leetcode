// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

func selfDivisiblePermutationCount(n int) int {
	ans := 0
	used := make([]bool, n+1)
	var dfs func(int)
	dfs = func(pos int) {
		if pos > n {
			ans++
			return
		}
		for v := 1; v <= n; v++ {
			if used[v] {
				continue
			}
			if v%pos != 0 && pos%v != 0 {
				continue
			}
			used[v] = true
			dfs(pos + 1)
			used[v] = false
		}
	}
	dfs(1)
	return ans
}
