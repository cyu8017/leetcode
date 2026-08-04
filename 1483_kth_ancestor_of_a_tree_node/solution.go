// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

type TreeAncestor struct {
	up [][]int
}

func Constructor(n int, parent []int) TreeAncestor {
	width := 1
	for (1 << width) < n {
		width++
	}
	up := make([][]int, width)
	up[0] = append([]int(nil), parent...)
	for b := 1; b < width; b++ {
		up[b] = make([]int, n)
		for i := 0; i < n; i++ {
			p := up[b-1][i]
			if p == -1 {
				up[b][i] = -1
			} else {
				up[b][i] = up[b-1][p]
			}
		}
	}
	return TreeAncestor{up: up}
}

func (this *TreeAncestor) GetKthAncestor(node int, k int) int {
	bit := 0
	for k > 0 && node != -1 {
		if k&1 == 1 {
			if bit >= len(this.up) {
				return -1
			}
			node = this.up[bit][node]
		}
		bit++
		k >>= 1
	}
	return node
}
