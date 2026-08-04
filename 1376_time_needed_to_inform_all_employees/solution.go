// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	children := make([][]int, n)
	for i, p := range manager {
		if p != -1 {
			children[p] = append(children[p], i)
		}
	}
	var dfs func(int) int
	dfs = func(u int) int {
		best := 0
		for _, v := range children[u] {
			if t := dfs(v); t > best {
				best = t
			}
		}
		return informTime[u] + best
	}
	return dfs(headID)
}
