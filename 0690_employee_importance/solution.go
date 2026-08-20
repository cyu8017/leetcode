// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

type Employee struct {
	Id           int
	Importance   int
	Subordinates []int
}

func getImportance(employees []*Employee, id int) int {
	table := map[int]*Employee{}
	for _, emp := range employees {
		table[emp.Id] = emp
	}
	var dfs func(eid int) int
	dfs = func(eid int) int {
		emp := table[eid]
		total := emp.Importance
		for _, sub := range emp.Subordinates {
			total += dfs(sub)
		}
		return total
	}
	return dfs(id)
}
