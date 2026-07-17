// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findDistance(root *TreeNode, p int, q int) int {
    graph := make(map[int][]int)
    var dfs func(node, parent *TreeNode)
    dfs = func(node, parent *TreeNode) {
        if node == nil {
            return
        }
        if _, ok := graph[node.Val]; !ok {
            graph[node.Val] = nil
        }
        if parent != nil {
            graph[node.Val] = append(graph[node.Val], parent.Val)
            graph[parent.Val] = append(graph[parent.Val], node.Val)
        }
        dfs(node.Left, node)
        dfs(node.Right, node)
    }
    dfs(root, nil)
    type entry struct {
        node, dist int
    }
    queue := []entry{{p, 0}}
    seen := map[int]bool{p: true}
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        if cur.node == q {
            return cur.dist
        }
        for _, nei := range graph[cur.node] {
            if !seen[nei] {
                seen[nei] = true
                queue = append(queue, entry{nei, cur.dist + 1})
            }
        }
    }
    return -1
}
