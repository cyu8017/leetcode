// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

import (
	"strconv"
	"strings"
)

type Node struct {
	Val      int
	Children []*Node
}

type Codec struct{}

func (this *Codec) Serialize(root *Node) string {
	if root == nil {
		return ""
	}

	parts := make([]string, 0)
	queue := []*Node{root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		parts = append(parts, strconv.Itoa(node.Val))
		parts = append(parts, strconv.Itoa(len(node.Children)))
		for _, child := range node.Children {
			parts = append(parts, strconv.Itoa(child.Val))
			queue = append(queue, child)
		}
	}

	return strings.Join(parts, ",")
}

func (this *Codec) Deserialize(data string) *Node {
	if data == "" {
		return nil
	}

	values := strings.Split(data, ",")
	index := 0

	readRoot := func() *Node {
		value, _ := strconv.Atoi(values[index])
		childCount, _ := strconv.Atoi(values[index+1])
		index += 2
		node := &Node{Val: value, Children: make([]*Node, 0, childCount)}
		for child := 0; child < childCount; child++ {
			childValue, _ := strconv.Atoi(values[index])
			node.Children = append(node.Children, &Node{Val: childValue})
			index++
		}
		return node
	}

	root := readRoot()
	queue := append([]*Node(nil), root.Children...)

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		value, _ := strconv.Atoi(values[index])
		childCount, _ := strconv.Atoi(values[index+1])
		index += 2
		if value != node.Val {
			return nil
		}
		for child := 0; child < childCount; child++ {
			childValue, _ := strconv.Atoi(values[index])
			childNode := &Node{Val: childValue}
			node.Children = append(node.Children, childNode)
			queue = append(queue, childNode)
			index++
		}
	}

	return root
}
