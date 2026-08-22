// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

func generateSchedule(n int) [][]int {
	if n < 5 {
		return [][]int{}
	}
	var matches [][]int
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i != j {
				matches = append(matches, []int{i, j})
			}
		}
	}
	used := make([]bool, len(matches))
	var sched [][]int
	last0, last1 := -1, -1
	var dfs func() bool
	dfs = func() bool {
		if len(sched) == len(matches) {
			return true
		}
		for i, m := range matches {
			if used[i] {
				continue
			}
			if m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1 {
				continue
			}
			used[i] = true
			sched = append(sched, m)
			p0, p1 := last0, last1
			last0, last1 = m[0], m[1]
			if dfs() {
				return true
			}
			last0, last1 = p0, p1
			sched = sched[:len(sched)-1]
			used[i] = false
		}
		return false
	}
	if dfs() {
		return sched
	}
	return [][]int{}
}
