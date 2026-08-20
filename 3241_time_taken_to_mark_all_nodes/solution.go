// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

type markNode struct {
	node int
	time int
}

type top2 struct {
	top1 markNode
	top2 markNode
}

func timeTaken(edges [][]int) []int {
	n := len(edges) + 1
	ans := make([]int, n)
	tree := make([][]int, n)
	dp := make([]top2, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		tree[u] = append(tree[u], v)
		tree[v] = append(tree[v], u)
	}
	var getTime func(int) int
	getTime = func(u int) int {
		if u%2 == 0 {
			return 2
		}
		return 1
	}
	var dfs func(u, prev int) int
	dfs = func(u, prev int) int {
		t1, t2 := markNode{}, markNode{}
		for _, v := range tree[u] {
			if v == prev {
				continue
			}
			t := dfs(v, u) + getTime(v)
			if t >= t1.time {
				t2 = t1
				t1 = markNode{v, t}
			} else if t > t2.time {
				t2 = markNode{v, t}
			}
		}
		dp[u] = top2{t1, t2}
		return t1.time
	}
	var reroot func(u, prev, maxTime int)
	reroot = func(u, prev, maxTime int) {
		ans[u] = maxTime
		if dp[u].top1.time > ans[u] {
			ans[u] = dp[u].top1.time
		}
		for _, v := range tree[u] {
			if v == prev {
				continue
			}
			side := dp[u].top1.time
			if dp[u].top1.node == v {
				side = dp[u].top2.time
			}
			newMax := maxTime
			if side > newMax {
				newMax = side
			}
			reroot(v, u, getTime(u)+newMax)
		}
	}
	dfs(0, -1)
	reroot(0, -1, 0)
	return ans
}
