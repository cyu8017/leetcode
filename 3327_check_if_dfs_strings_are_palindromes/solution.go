// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

func findAnswer(parent []int, s string) []bool {
	n := len(parent)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[parent[i]] = append(g[parent[i]], i)
	}
	for i := range g {
		// children already in ascending order if edges added in order? ensure sort
		// parent iteration i=1..n-1 gives ascending child ids
	}
	ans := make([]bool, n)
	var dfsStr func(int) string
	dfsStr = func(u int) string {
		out := []byte{}
		for _, v := range g[u] {
			out = append(out, dfsStr(v)...)
		}
		out = append(out, s[u])
		str := string(out)
		ans[u] = isPal(str)
		return str
	}
	dfsStr(0)
	return ans
}

func isPal(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
