// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/


func minReverseOperations(n int, p int, banned []int, k int) []int {
	ban := map[int]bool{}
	for _, x := range banned {
		ban[x] = true
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	ans[p] = 0
	// BFS over positions; for each pos, reachable via reverse of length k
	type node struct{ i, d int }
	q := []node{{p, 0}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		// endpoints of window of size k that contain cur.i
		lo := cur.i - (k - 1)
		if lo < 0 {
			lo = 0
		}
		hi := cur.i
		if hi > n-k {
			hi = n - k
		}
		for L := lo; L <= hi; L++ {
			R := L + k - 1
			ni := L + R - cur.i
			if ni < 0 || ni >= n || ban[ni] || ans[ni] != -1 {
				continue
			}
			ans[ni] = cur.d + 1
			q = append(q, node{ni, cur.d + 1})
		}
	}
	return ans
}
