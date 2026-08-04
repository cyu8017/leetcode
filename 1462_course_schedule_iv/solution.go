// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {
	reach := make([][]bool, numCourses)
	for i := range reach {
		reach[i] = make([]bool, numCourses)
	}
	for _, p := range prerequisites {
		reach[p[0]][p[1]] = true
	}
	for k := 0; k < numCourses; k++ {
		for i := 0; i < numCourses; i++ {
			if reach[i][k] {
				for j := 0; j < numCourses; j++ {
					reach[i][j] = reach[i][j] || reach[k][j]
				}
			}
		}
	}
	answer := make([]bool, len(queries))
	for i, q := range queries {
		answer[i] = reach[q[0]][q[1]]
	}
	return answer
}
