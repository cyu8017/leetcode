// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

func countVisitedNodes(edges []int) []int {
	n := len(edges)
	ans := make([]int, n)
	state := make([]int, n) // 0=unseen 1=visiting 2=done
	var stack []int
	var dfs func(int)
	dfs = func(u int) {
		state[u] = 1
		stack = append(stack, u)
		v := edges[u]
		if state[v] == 0 {
			dfs(v)
		} else if state[v] == 1 {
			// cycle
			idx := len(stack) - 1
			for stack[idx] != v {
				idx--
			}
			cyc := len(stack) - idx
			for i := idx; i < len(stack); i++ {
				ans[stack[i]] = cyc
			}
		}
		if ans[u] == 0 {
			ans[u] = ans[edges[u]] + 1
		}
		state[u] = 2
		stack = stack[:len(stack)-1]
	}
	for i := 0; i < n; i++ {
		if state[i] == 0 {
			dfs(i)
		}
	}
	return ans
}
