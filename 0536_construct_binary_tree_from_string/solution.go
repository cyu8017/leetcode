// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func str2tree(s string) *TreeNode {
	if s == "" {
		return nil
	}

	index := 0
	var parse func() *TreeNode
	parse = func() *TreeNode {
		if index >= len(s) {
			return nil
		}

		sign := 1
		if s[index] == '-' {
			sign = -1
			index++
		}

		value := 0
		for index < len(s) && s[index] >= '0' && s[index] <= '9' {
			value = value*10 + int(s[index]-'0')
			index++
		}

		node := &TreeNode{Val: sign * value}

		if index < len(s) && s[index] == '(' {
			index++
			node.Left = parse()
			index++
		}

		if index < len(s) && s[index] == '(' {
			index++
			node.Right = parse()
			index++
		}

		return node
	}

	return parse()
}
