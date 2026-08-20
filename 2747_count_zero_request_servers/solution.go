// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/


import "sort"

func countServers(n int, logs [][]int, x int, queries []int) []int {
	sort.Slice(logs, func(i, j int) bool { return logs[i][1] < logs[j][1] })
	type qi struct{ t, i int }
	qs := make([]qi, len(queries))
	for i, t := range queries {
		qs[i] = qi{t, i}
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].t < qs[j].t })
	ans := make([]int, len(queries))
	cnt := map[int]int{}
	active := 0
	l, r := 0, 0
	for _, q := range qs {
		for r < len(logs) && logs[r][1] <= q.t {
			id := logs[r][0]
			if cnt[id] == 0 {
				active++
			}
			cnt[id]++
			r++
		}
		for l < r && logs[l][1] < q.t-x {
			id := logs[l][0]
			cnt[id]--
			if cnt[id] == 0 {
				active--
			}
			l++
		}
		ans[q.i] = n - active
	}
	return ans
}
