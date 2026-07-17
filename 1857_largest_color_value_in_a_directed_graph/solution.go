// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

func largestPathValue(colors string, edges [][]int) int {
	n := len(colors)
	indegree := make([]int, n)
	adjacency := make([][]int, n)

	for _, edge := range edges {
		fromNode, toNode := edge[0], edge[1]
		adjacency[fromNode] = append(adjacency[fromNode], toNode)
		indegree[toNode]++
	}

	queue := make([]int, 0)
	for node := 0; node < n; node++ {
		if indegree[node] == 0 {
			queue = append(queue, node)
		}
	}

	dp := make([][]int, n)
	for node := 0; node < n; node++ {
		dp[node] = make([]int, 26)
		dp[node][int(colors[node]-'a')] = 1
	}

	processed := 0
	answer := 0

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		processed++

		for colorIndex := 0; colorIndex < 26; colorIndex++ {
			if dp[node][colorIndex] > answer {
				answer = dp[node][colorIndex]
			}
		}

		for _, neighbor := range adjacency[node] {
			neighborColor := int(colors[neighbor] - 'a')
			for colorIndex := 0; colorIndex < 26; colorIndex++ {
				candidate := dp[node][colorIndex]
				if colorIndex == neighborColor {
					candidate++
				}
				if candidate > dp[neighbor][colorIndex] {
					dp[neighbor][colorIndex] = candidate
				}
			}
			indegree[neighbor]--
			if indegree[neighbor] == 0 {
				queue = append(queue, neighbor)
			}
		}
	}

	if processed != n {
		return -1
	}
	return answer
}
