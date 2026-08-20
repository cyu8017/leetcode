// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/


import "sort"

func maximumSumQueries(nums1 []int, nums2 []int, queries [][]int) []int {
	n := len(nums1)
	type pair struct{ x, y, s int }
	pts := make([]pair, n)
	for i := 0; i < n; i++ {
		pts[i] = pair{nums1[i], nums2[i], nums1[i] + nums2[i]}
	}
	sort.Slice(pts, func(i, j int) bool { return pts[i].x > pts[j].x })
	type qi struct{ x, y, i int }
	qs := make([]qi, len(queries))
	for i, q := range queries {
		qs[i] = qi{q[0], q[1], i}
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].x > qs[j].x })
	// compress y
	ys := append([]int(nil), nums2...)
	for _, q := range queries {
		ys = append(ys, q[1])
	}
	sort.Ints(ys)
	uniq := []int{}
	for _, y := range ys {
		if len(uniq) == 0 || uniq[len(uniq)-1] != y {
			uniq = append(uniq, y)
		}
	}
	rank := map[int]int{}
	for i, y := range uniq {
		rank[y] = i + 1
	}
	m := len(uniq)
	bit := make([]int, m+2)
	update := func(i, v int) {
		for i <= m {
			if v > bit[i] {
				bit[i] = v
			}
			i += i & -i
		}
	}
	query := func(i int) int {
		best := -1
		for i > 0 {
			if bit[i] > best {
				best = bit[i]
			}
			i -= i & -i
		}
		return best
	}
	ans := make([]int, len(queries))
	j := 0
	for _, q := range qs {
		for j < n && pts[j].x >= q.x {
			update(m-rank[pts[j].y]+1, pts[j].s)
			j++
		}
		ans[q.i] = query(m - rank[q.y] + 1)
	}
	return ans
}
