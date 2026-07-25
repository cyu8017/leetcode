// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

import "strconv"

type Node struct {
	Val   string
	Left  *Node
	Right *Node
}

func (this *Node) Evaluate() int {
	if this.Val != "+" && this.Val != "-" && this.Val != "*" && this.Val != "/" {
		v, _ := strconv.Atoi(this.Val)
		return v
	}
	a, b := this.Left.Evaluate(), this.Right.Evaluate()
	switch this.Val {
	case "+":
		return a + b
	case "-":
		return a - b
	case "*":
		return a * b
	default:
		return a / b
	}
}

type TreeBuilder struct{}

func Constructor() TreeBuilder {
	return TreeBuilder{}
}

func (this *TreeBuilder) ExpTree(postfix []string) *Node {
	stack := []*Node{}
	for _, token := range postfix {
		node := &Node{Val: token}
		if token == "+" || token == "-" || token == "*" || token == "/" {
			node.Right = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			node.Left = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, node)
	}
	return stack[len(stack)-1]
}
