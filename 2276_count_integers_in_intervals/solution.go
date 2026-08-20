// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

type CountIntervals struct {
	root *segNode
	cnt  int
}

type segNode struct {
	left, right *segNode
	covered     bool
}

func Constructor() CountIntervals {
	return CountIntervals{}
}

func (this *CountIntervals) Add(left int, right int) {
	this.cnt += add(1, 1000000000, left, right, &this.root)
}

func (this *CountIntervals) Count() int {
	return this.cnt
}

func add(L, R, l, r int, node **segNode) int {
	if *node == nil {
		*node = &segNode{}
	}
	n := *node
	if n.covered {
		return 0
	}
	if l <= L && R <= r {
		n.covered = true
		n.left, n.right = nil, nil
		return R - L + 1
	}
	mid := (L + R) / 2
	added := 0
	if l <= mid {
		added += add(L, mid, l, r, &n.left)
	}
	if r > mid {
		added += add(mid+1, R, l, r, &n.right)
	}
	if n.left != nil && n.right != nil && n.left.covered && n.right.covered {
		n.covered = true
		n.left, n.right = nil, nil
	}
	return added
}
