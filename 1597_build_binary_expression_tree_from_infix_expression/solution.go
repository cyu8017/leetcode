// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

type Node struct {
	Val   byte
	Left  *Node
	Right *Node
}

func expTree(s string) *Node {
	nodes := []*Node{}
	ops := []byte{}
	priority := map[byte]int{'+': 1, '-': 1, '*': 2, '/': 2}
	apply := func() {
		op := ops[len(ops)-1]
		ops = ops[:len(ops)-1]
		right := nodes[len(nodes)-1]
		nodes = nodes[:len(nodes)-1]
		left := nodes[len(nodes)-1]
		nodes = nodes[:len(nodes)-1]
		nodes = append(nodes, &Node{Val: op, Left: left, Right: right})
	}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch >= '0' && ch <= '9' {
			nodes = append(nodes, &Node{Val: ch})
		} else if ch == '(' {
			ops = append(ops, ch)
		} else if ch == ')' {
			for ops[len(ops)-1] != '(' {
				apply()
			}
			ops = ops[:len(ops)-1]
		} else {
			for len(ops) > 0 && ops[len(ops)-1] != '(' && priority[ops[len(ops)-1]] >= priority[ch] {
				apply()
			}
			ops = append(ops, ch)
		}
	}
	for len(ops) > 0 {
		apply()
	}
	return nodes[0]
}
