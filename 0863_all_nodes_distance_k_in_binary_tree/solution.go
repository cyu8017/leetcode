// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func distanceK(root *TreeNode, target *TreeNode, k int) []int {
	graph := map[*TreeNode][]*TreeNode{}
	var build func(node, parent *TreeNode)
	build = func(node, parent *TreeNode) {
		if node == nil {
			return
		}
		if parent != nil {
			graph[node] = append(graph[node], parent)
			graph[parent] = append(graph[parent], node)
		}
		build(node.Left, node)
		build(node.Right, node)
	}
	build(root, nil)
	type item struct {
		node *TreeNode
		dist int
	}
	queue := []item{{target, 0}}
	seen := map[*TreeNode]bool{target: true}
	ans := []int{}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.dist == k {
			ans = append(ans, cur.node.Val)
			continue
		}
		for _, nei := range graph[cur.node] {
			if !seen[nei] {
				seen[nei] = true
				queue = append(queue, item{nei, cur.dist + 1})
			}
		}
	}
	return ans
}
