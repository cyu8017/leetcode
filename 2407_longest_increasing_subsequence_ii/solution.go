// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

type SegTree struct {
	n    int
	tree []int
}

func NewSegTree(n int) *SegTree {
	return &SegTree{n: n, tree: make([]int, 4*n)}
}

func (st *SegTree) update(idx, l, r, pos, val int) {
	if l == r {
		if val > st.tree[idx] {
			st.tree[idx] = val
		}
		return
	}
	mid := (l + r) / 2
	if pos <= mid {
		st.update(idx*2, l, mid, pos, val)
	} else {
		st.update(idx*2+1, mid+1, r, pos, val)
	}
	st.tree[idx] = st.tree[idx*2]
	if st.tree[idx*2+1] > st.tree[idx] {
		st.tree[idx] = st.tree[idx*2+1]
	}
}

func (st *SegTree) query(idx, l, r, ql, qr int) int {
	if qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return st.tree[idx]
	}
	mid := (l + r) / 2
	a := st.query(idx*2, l, mid, ql, qr)
	b := st.query(idx*2+1, mid+1, r, ql, qr)
	if a > b {
		return a
	}
	return b
}

func lengthOfLIS(nums []int, k int) int {
	maxV := 0
	for _, x := range nums {
		if x > maxV {
			maxV = x
		}
	}
	st := NewSegTree(maxV + 1)
	ans := 0
	for _, x := range nums {
		lo := x - k
		if lo < 1 {
			lo = 1
		}
		best := 1
		if lo <= x-1 {
			best = st.query(1, 1, maxV, lo, x-1) + 1
		}
		st.update(1, 1, maxV, x, best)
		if best > ans {
			ans = best
		}
	}
	return ans
}
