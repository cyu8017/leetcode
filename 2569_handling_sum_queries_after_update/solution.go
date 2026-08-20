// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/


func handleQuery(nums1 []int, nums2 []int, queries [][]int) []int64 {
	n := len(nums1)
	// segment tree for nums1 flip + ones count
	ones := make([]int, 4*n)
	lazy := make([]bool, 4*n)
	var build func(idx, l, r int)
	build = func(idx, l, r int) {
		if l == r {
			ones[idx] = nums1[l]
			return
		}
		m := (l + r) / 2
		build(idx*2, l, m)
		build(idx*2+1, m+1, r)
		ones[idx] = ones[idx*2] + ones[idx*2+1]
	}
	var apply func(idx, l, r int)
	apply = func(idx, l, r int) {
		ones[idx] = (r - l + 1) - ones[idx]
		lazy[idx] = !lazy[idx]
	}
	var push func(idx, l, r int)
	push = func(idx, l, r int) {
		if lazy[idx] && l != r {
			m := (l + r) / 2
			apply(idx*2, l, m)
			apply(idx*2+1, m+1, r)
			lazy[idx] = false
		}
	}
	var update func(idx, l, r, ql, qr int)
	update = func(idx, l, r, ql, qr int) {
		if ql <= l && r <= qr {
			apply(idx, l, r)
			return
		}
		push(idx, l, r)
		m := (l + r) / 2
		if ql <= m {
			update(idx*2, l, m, ql, qr)
		}
		if qr > m {
			update(idx*2+1, m+1, r, ql, qr)
		}
		ones[idx] = ones[idx*2] + ones[idx*2+1]
	}
	build(1, 0, n-1)
	sum2 := int64(0)
	for _, x := range nums2 {
		sum2 += int64(x)
	}
	ans := []int64{}
	for _, q := range queries {
		if q[0] == 1 {
			update(1, 0, n-1, q[1], q[2])
		} else if q[0] == 2 {
			sum2 += int64(q[1]) * int64(ones[1])
		} else {
			ans = append(ans, sum2)
		}
	}
	return ans
}
