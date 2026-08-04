// LeetCode 1938 - Maximum Genetic Difference Query
// https://leetcode.com/problems/maximum-genetic-difference-query/

type trieNode1938 struct {
	child [2]*trieNode1938
	cnt   int
}

func maxGeneticDifference(parents []int, queries [][]int) []int {
	n := len(parents)
	children := make([][]int, n)
	root := 0
	for i, p := range parents {
		if p == -1 {
			root = i
		} else {
			children[p] = append(children[p], i)
		}
	}
	qmap := make([][][2]int, n)
	for i, q := range queries {
		qmap[q[0]] = append(qmap[q[0]], [2]int{i, q[1]})
	}
	ans := make([]int, len(queries))
	trieRoot := &trieNode1938{}
	const BITS = 17

	trieUpdate := func(num, delta int) {
		node := trieRoot
		for b := BITS; b >= 0; b-- {
			bit := (num >> b) & 1
			if node.child[bit] == nil {
				node.child[bit] = &trieNode1938{}
			}
			node = node.child[bit]
			node.cnt += delta
		}
	}
	trieMaxXor := func(num int) int {
		node := trieRoot
		res := 0
		for b := BITS; b >= 0; b-- {
			bit := (num >> b) & 1
			want := 1 - bit
			if node.child[want] != nil && node.child[want].cnt > 0 {
				res |= 1 << b
				node = node.child[want]
			} else {
				node = node.child[bit]
			}
		}
		return res
	}
	var dfs func(u int)
	dfs = func(u int) {
		trieUpdate(u, 1)
		for _, qi := range qmap[u] {
			ans[qi[0]] = trieMaxXor(qi[1])
		}
		for _, v := range children[u] {
			dfs(v)
		}
		trieUpdate(u, -1)
	}
	dfs(root)
	return ans
}
