// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findClosestLeaf(root *TreeNode, k int) int {
	graph := map[int][]int{}
	leaves := map[int]bool{}
	var build func(node, parent *TreeNode)
	build = func(node, parent *TreeNode) {
		if node == nil {
			return
		}
		if parent != nil {
			graph[node.Val] = append(graph[node.Val], parent.Val)
			graph[parent.Val] = append(graph[parent.Val], node.Val)
		}
		if node.Left == nil && node.Right == nil {
			leaves[node.Val] = true
		}
		build(node.Right, node)
		build(node.Left, node)
	}
	build(root, nil)
	queue := []int{k}
	seen := map[int]bool{k: true}
	for len(queue) > 0 {
		value := queue[0]
		queue = queue[1:]
		if leaves[value] {
			return value
		}
		for _, neighbor := range graph[value] {
			if !seen[neighbor] {
				seen[neighbor] = true
				queue = append(queue, neighbor)
			}
		}
	}
	return -1
}
