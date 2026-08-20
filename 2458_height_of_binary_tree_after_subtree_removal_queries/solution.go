// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func treeQueries(root *TreeNode, queries []int) []int {
	height := map[int]int{}
	level := map[int]int{}
	levelMax := map[int][]int{} // top 2 heights per level
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, d int) int {
		if node == nil {
			return -1
		}
		level[node.Val] = d
		h := 1 + max(dfs(node.Left, d+1), dfs(node.Right, d+1))
		height[node.Val] = h
		arr := levelMax[d]
		if len(arr) == 0 {
			levelMax[d] = []int{h}
		} else if h >= arr[0] {
			levelMax[d] = []int{h, arr[0]}
		} else if len(arr) == 1 || h > arr[1] {
			levelMax[d] = []int{arr[0], h}
		}
		return h
	}
	dfs(root, 0)
	ans := make([]int, len(queries))
	for i, q := range queries {
		d := level[q]
		h := height[q]
		top := levelMax[d]
		if top[0] == h {
			if len(top) > 1 {
				ans[i] = d + top[1]
			} else {
				ans[i] = d - 1
			}
		} else {
			ans[i] = d + top[0]
		}
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
