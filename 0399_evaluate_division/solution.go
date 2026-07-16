// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

func calcEquation(
	equations [][]string,
	values []float64,
	queries [][]string,
) []float64 {
	graph := make(map[string]map[string]float64)

	for index, equation := range equations {
		dividend := equation[0]
		divisor := equation[1]
		if graph[dividend] == nil {
			graph[dividend] = make(map[string]float64)
		}
		if graph[divisor] == nil {
			graph[divisor] = make(map[string]float64)
		}
		graph[dividend][divisor] = values[index]
		graph[divisor][dividend] = 1.0 / values[index]
	}

	var dfs func(start string, end string, visited map[string]bool) float64
	dfs = func(start string, end string, visited map[string]bool) float64 {
		if graph[start] == nil || graph[end] == nil {
			return -1.0
		}
		if start == end {
			return 1.0
		}
		visited[start] = true
		for neighbor, weight := range graph[start] {
			if visited[neighbor] {
				continue
			}
			result := dfs(neighbor, end, visited)
			if result != -1.0 {
				return weight * result
			}
		}
		return -1.0
	}

	answers := make([]float64, len(queries))
	for index, query := range queries {
		visited := make(map[string]bool)
		answers[index] = dfs(query[0], query[1], visited)
	}
	return answers
}
