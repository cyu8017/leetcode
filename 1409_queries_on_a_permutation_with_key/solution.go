// LeetCode 1409 - Queries on a Permutation With Key
// https://leetcode.com/problems/queries-on-a-permutation-with-key/

func processQueries(queries []int, m int) []int {
	values := make([]int, m)
	for i := 0; i < m; i++ {
		values[i] = i + 1
	}
	answer := make([]int, len(queries))
	for qi, query := range queries {
		index := 0
		for i, v := range values {
			if v == query {
				index = i
				break
			}
		}
		answer[qi] = index
		val := values[index]
		copy(values[1:index+1], values[:index])
		values[0] = val
	}
	return answer
}
