// LeetCode 0113 - Path Sum II
type TreeNode struct { Val int; Left, Right *TreeNode }
func pathSum(root *TreeNode, targetSum int) [][]int {
	var out [][]int
	var dfs func(*TreeNode, int, []int)
	dfs = func(n *TreeNode, sum int, path []int) {
		if n == nil { return }; path = append(path, n.Val); sum -= n.Val
		if n.Left == nil && n.Right == nil && sum == 0 {
			out = append(out, append([]int(nil), path...)); return
		}
		dfs(n.Left, sum, path); dfs(n.Right, sum, path)
	}
	dfs(root, targetSum, nil); return out
}