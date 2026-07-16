// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

import (
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Codec struct{}

func (this *Codec) Serialize(root *TreeNode) string {
	parts := make([]string, 0)

	var preorder func(node *TreeNode)
	preorder = func(node *TreeNode) {
		if node == nil {
			parts = append(parts, "#")
			return
		}
		parts = append(parts, strconv.Itoa(node.Val))
		preorder(node.Left)
		preorder(node.Right)
	}

	preorder(root)
	return strings.Join(parts, ",")
}

func (this *Codec) Deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}

	values := strings.Split(data, ",")
	index := 0

	var build func() *TreeNode
	build = func() *TreeNode {
		token := values[index]
		index++
		if token == "#" {
			return nil
		}
		val, _ := strconv.Atoi(token)
		node := &TreeNode{Val: val}
		node.Left = build()
		node.Right = build()
		return node
	}

	return build()
}
