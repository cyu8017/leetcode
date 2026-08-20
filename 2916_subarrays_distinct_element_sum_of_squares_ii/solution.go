// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

func sumCounts(nums []int) int {
	const mod = 1_000_000_007
	n := len(nums)
	// segment tree for range add and range sum of values and squares
	// Simplified O(n^2) may TLE but for local cases ok; use online formula
	last := map[int]int{}
	type node struct{ sum, sumSq, lazy int }
	tree := make([]node, 4*(n+2))
	var apply func(int, int, int, int)
	apply = func(idx, l, r, val int) {
		length := r - l + 1
		tree[idx].sumSq = (tree[idx].sumSq + 2*val%mod*tree[idx].sum%mod + val%mod*val%mod*length%mod) % mod
		tree[idx].sum = (tree[idx].sum + val%mod*length%mod) % mod
		tree[idx].lazy = (tree[idx].lazy + val) % mod
	}
	var push func(int, int, int)
	push = func(idx, l, r int) {
		if tree[idx].lazy != 0 && l != r {
			mid := (l + r) / 2
			apply(idx*2, l, mid, tree[idx].lazy)
			apply(idx*2+1, mid+1, r, tree[idx].lazy)
			tree[idx].lazy = 0
		}
	}
	var update func(int, int, int, int, int, int)
	update = func(idx, l, r, ql, qr, val int) {
		if ql > r || qr < l {
			return
		}
		if ql <= l && r <= qr {
			apply(idx, l, r, val)
			return
		}
		push(idx, l, r)
		mid := (l + r) / 2
		update(idx*2, l, mid, ql, qr, val)
		update(idx*2+1, mid+1, r, ql, qr, val)
		tree[idx].sum = (tree[idx*2].sum + tree[idx*2+1].sum) % mod
		tree[idx].sumSq = (tree[idx*2].sumSq + tree[idx*2+1].sumSq) % mod
	}
	ans := 0
	for i := 1; i <= n; i++ {
		v := nums[i-1]
		prev := last[v]
		update(1, 1, n, prev+1, i, 1)
		ans = (ans + tree[1].sumSq) % mod
		last[v] = i
	}
	return ans
}
