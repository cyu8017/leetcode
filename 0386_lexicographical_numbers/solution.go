// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

func lexicalOrder(n int) []int {
	result := make([]int, 0, n)

	var dfs func(current int)
	dfs = func(current int) {
		if current > n {
			return
		}
		result = append(result, current)
		dfs(current * 10)
		if current%10 < 9 {
			dfs(current + 1)
		}
	}

	dfs(1)
	return result
}
