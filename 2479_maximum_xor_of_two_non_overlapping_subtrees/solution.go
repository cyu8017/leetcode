// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

func maxXor(n int, edges [][]int, values []int) int64 {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	sum := make([]int64, n)
	var dfsSum func(u, p int) int64
	dfsSum = func(u, p int) int64 {
		s := int64(values[u])
		for _, v := range g[u] {
			if v != p {
				s += dfsSum(v, u)
			}
		}
		sum[u] = s
		return s
	}
	dfsSum(0, -1)
	type trie struct {
		child [2]*trie
	}
	root := &trie{}
	insert := func(x int64) {
		cur := root
		for b := 46; b >= 0; b-- {
			bit := int((x >> b) & 1)
			if cur.child[bit] == nil {
				cur.child[bit] = &trie{}
			}
			cur = cur.child[bit]
		}
	}
	query := func(x int64) int64 {
		cur := root
		if cur.child[0] == nil && cur.child[1] == nil {
			return 0
		}
		var ans int64
		for b := 46; b >= 0; b-- {
			bit := int((x >> b) & 1)
			want := bit ^ 1
			if cur.child[want] != nil {
				ans |= 1 << b
				cur = cur.child[want]
			} else if cur.child[bit] != nil {
				cur = cur.child[bit]
			} else {
				return ans
			}
		}
		return ans
	}
	var ans int64
	var dfs func(u, p int)
	dfs = func(u, p int) {
		for _, v := range g[u] {
			if v == p {
				continue
			}
			xor := query(sum[v])
			if xor > ans {
				ans = xor
			}
			dfs(v, u)
			insert(sum[v])
		}
	}
	dfs(0, -1)
	return ans
}
