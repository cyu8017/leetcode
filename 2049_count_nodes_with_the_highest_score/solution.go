// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

func countHighestScoreNodes(parents []int) int {
	n := len(parents)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		children[parents[i]] = append(children[parents[i]], i)
	}
	size := make([]int, n)
	var dfs func(int) int
	dfs = func(u int) int {
		size[u] = 1
		for _, v := range children[u] {
			size[u] += dfs(v)
		}
		return size[u]
	}
	dfs(0)
	best, ans := int64(0), 0
	for u := 0; u < n; u++ {
		score := int64(1)
		for _, v := range children[u] {
			score *= int64(size[v])
		}
		up := n - size[u]
		if up > 0 {
			score *= int64(up)
		}
		if score > best {
			best = score
			ans = 1
		} else if score == best {
			ans++
		}
	}
	return ans
}
