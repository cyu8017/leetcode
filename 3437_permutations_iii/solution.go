// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

func permute(n int) [][]int {
	ans := [][]int{}
	used := make([]bool, n+1)
	cur := []int{}
	var dfs func()
	dfs = func() {
		if len(cur) == n {
			ans = append(ans, append([]int(nil), cur...))
			return
		}
		for i := 1; i <= n; i++ {
			if used[i] {
				continue
			}
			if len(cur) > 0 && (cur[len(cur)-1]%2 == i%2) {
				continue
			}
			used[i] = true
			cur = append(cur, i)
			dfs()
			cur = cur[:len(cur)-1]
			used[i] = false
		}
	}
	dfs()
	return ans
}
