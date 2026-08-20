// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

func countPalindromePaths(parent []int, s string) int64 {
	n := len(parent)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[parent[i]] = append(g[parent[i]], i)
	}
	freq := map[int]int{0: 1}
	var ans int64
	var dfs func(int, int)
	dfs = func(u, mask int) {
		for _, v := range g[u] {
			nm := mask ^ (1 << (s[v] - 'a'))
			ans += int64(freq[nm])
			for b := 0; b < 26; b++ {
				ans += int64(freq[nm^(1<<b)])
			}
			freq[nm]++
			dfs(v, nm)
		}
	}
	dfs(0, 0)
	return ans
}
