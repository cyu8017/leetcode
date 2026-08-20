// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func allPossibleFBT(n int) []*TreeNode {
	memo := map[int][]*TreeNode{}
	var build func(nodes int) []*TreeNode
	build = func(nodes int) []*TreeNode {
		if nodes%2 == 0 {
			return nil
		}
		if nodes == 1 {
			return []*TreeNode{{Val: 0}}
		}
		if cached, ok := memo[nodes]; ok {
			return cached
		}
		res := []*TreeNode{}
		for left := 1; left < nodes; left += 2 {
			right := nodes - 1 - left
			for _, L := range build(left) {
				for _, R := range build(right) {
					res = append(res, &TreeNode{Val: 0, Left: L, Right: R})
				}
			}
		}
		memo[nodes] = res
		return res
	}
	return build(n)
}
