// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func amountOfTime(root *TreeNode, start int) int {
	g := map[int][]int{}
	var build func(*TreeNode, *TreeNode)
	build = func(node, parent *TreeNode) {
		if node == nil {
			return
		}
		if parent != nil {
			g[node.Val] = append(g[node.Val], parent.Val)
			g[parent.Val] = append(g[parent.Val], node.Val)
		}
		build(node.Left, node)
		build(node.Right, node)
	}
	build(root, nil)
	ans := 0
	vis := map[int]bool{start: true}
	type item struct{ v, d int }
	q := []item{{start, 0}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.d > ans {
			ans = cur.d
		}
		for _, nxt := range g[cur.v] {
			if !vis[nxt] {
				vis[nxt] = true
				q = append(q, item{nxt, cur.d + 1})
			}
		}
	}
	return ans
}
