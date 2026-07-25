// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

type Node struct {
	Val   byte
	Left  *Node
	Right *Node
}

func checkEquivalence(root1 *Node, root2 *Node) bool {
	a := make([]int, 26)
	b := make([]int, 26)
	count(root1, a)
	count(root2, b)
	for i := 0; i < 26; i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func count(node *Node, out []int) {
	if node == nil {
		return
	}
	if node.Val == '+' {
		count(node.Left, out)
		count(node.Right, out)
	} else {
		out[node.Val-'a']++
	}
}
