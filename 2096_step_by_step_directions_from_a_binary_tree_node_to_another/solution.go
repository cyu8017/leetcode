// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getDirections(root *TreeNode, startValue int, destValue int) string {
	var path func(*TreeNode, int, *[]byte) bool
	path = func(node *TreeNode, target int, p *[]byte) bool {
		if node == nil {
			return false
		}
		if node.Val == target {
			return true
		}
		*p = append(*p, 'L')
		if path(node.Left, target, p) {
			return true
		}
		(*p)[len(*p)-1] = 'R'
		if path(node.Right, target, p) {
			return true
		}
		*p = (*p)[:len(*p)-1]
		return false
	}
	var ps, pd []byte
	path(root, startValue, &ps)
	path(root, destValue, &pd)
	i := 0
	for i < len(ps) && i < len(pd) && ps[i] == pd[i] {
		i++
	}
	up := make([]byte, len(ps)-i)
	for j := range up {
		up[j] = 'U'
	}
	return string(up) + string(pd[i:])
}
