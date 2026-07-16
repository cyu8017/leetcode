// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

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
	if root == nil {
		return ""
	}

	values := make([]string, 0)
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node == nil {
			values = append(values, "")
		} else {
			values = append(values, strconv.Itoa(node.Val))
			queue = append(queue, node.Left, node.Right)
		}
	}

	for len(values) > 0 && values[len(values)-1] == "" {
		values = values[:len(values)-1]
	}

	return strings.Join(values, ",")
}

func (this *Codec) Deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}

	values := strings.Split(data, ",")
	rootVal, _ := strconv.Atoi(values[0])
	root := &TreeNode{Val: rootVal}
	queue := []*TreeNode{root}
	index := 1

	for len(queue) > 0 && index < len(values) {
		node := queue[0]
		queue = queue[1:]

		if index < len(values) && values[index] != "" {
			leftVal, _ := strconv.Atoi(values[index])
			node.Left = &TreeNode{Val: leftVal}
			queue = append(queue, node.Left)
		}
		index++

		if index < len(values) && values[index] != "" {
			rightVal, _ := strconv.Atoi(values[index])
			node.Right = &TreeNode{Val: rightVal}
			queue = append(queue, node.Right)
		}
		index++
	}

	return root
}
