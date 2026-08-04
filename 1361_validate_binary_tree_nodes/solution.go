// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
	indeg := make([]int, n)
	for _, x := range append(append([]int{}, leftChild...), rightChild...) {
		if x != -1 {
			indeg[x]++
			if indeg[x] > 1 {
				return false
			}
		}
	}
	roots := []int{}
	for i, x := range indeg {
		if x == 0 {
			roots = append(roots, i)
		}
	}
	if len(roots) != 1 {
		return false
	}
	seen := map[int]bool{}
	st := roots
	for len(st) > 0 {
		u := st[len(st)-1]
		st = st[:len(st)-1]
		if seen[u] {
			return false
		}
		seen[u] = true
		for _, v := range []int{leftChild[u], rightChild[u]} {
			if v != -1 {
				st = append(st, v)
			}
		}
	}
	return len(seen) == n
}
