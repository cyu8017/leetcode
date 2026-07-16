// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

func maxPathSum(root *TreeNode) int {
    best := -1 << 31
    var gain func(*TreeNode) int
    gain = func(node *TreeNode) int { if node == nil { return 0 }; left,right := gain(node.Left),gain(node.Right); if left < 0 { left=0 }; if right < 0 { right=0 }; if node.Val+left+right > best { best=node.Val+left+right }; if left > right { return node.Val+left }; return node.Val+right }
    gain(root); return best
}