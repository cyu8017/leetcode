// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

func sumNumbers(root *TreeNode) int { var dfs func(*TreeNode,int) int; dfs=func(node *TreeNode, value int) int { if node==nil{return 0};value=value*10+node.Val;if node.Left==nil&&node.Right==nil{return value};return dfs(node.Left,value)+dfs(node.Right,value) };return dfs(root,0) }