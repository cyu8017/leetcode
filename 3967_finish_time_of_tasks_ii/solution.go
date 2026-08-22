// LeetCode 3967 - Finish Time of Tasks II
// https://leetcode.com/problems/finish-time-of-tasks-ii/

func minFinishTime(n int, edges [][]int, baseTime []int) int64 {
	type edge3967 struct{ to, reverse int }
	graph := make([][]edge3967, n)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		iu, iv := len(graph[u]), len(graph[v])
		graph[u] = append(graph[u], edge3967{v, iv})
		graph[v] = append(graph[v], edge3967{u, iu})
	}
	parent, parentEdge := make([]int, n), make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for edgeIndex, edge := range graph[u] {
			if parent[edge.to] == -2 {
				parent[edge.to] = u
				parentEdge[edge.to] = edge.reverse
				_ = edgeIndex
				order = append(order, edge.to)
			}
		}
	}
	incoming := make([][]int64, n)
	for i := range incoming {
		incoming[i] = make([]int64, len(graph[i]))
	}
	combine := func(minimum, maximum int64, count int, base int) int64 {
		if count == 0 {
			return int64(base)
		}
		return 2*maximum - minimum + int64(base)
	}
	for oi := n - 1; oi > 0; oi-- {
		u := order[oi]
		minimum, maximum, count := int64(1<<62), int64(-1), 0
		for edgeIndex, value := range incoming[u] {
			if edgeIndex == parentEdge[u] {
				continue
			}
			if value < minimum {
				minimum = value
			}
			if value > maximum {
				maximum = value
			}
			count++
		}
		value := combine(minimum, maximum, count, baseTime[u])
		parentNode := parent[u]
		reverseIndex := graph[u][parentEdge[u]].reverse
		incoming[parentNode][reverseIndex] = value
	}
	answer := int64(1 << 62)
	for _, u := range order {
		min1, min2, minIndex := int64(1<<62), int64(1<<62), -1
		max1, max2, maxIndex := int64(-1), int64(-1), -1
		for i, value := range incoming[u] {
			if value < min1 {
				min2, min1, minIndex = min1, value, i
			} else if value < min2 {
				min2 = value
			}
			if value > max1 {
				max2, max1, maxIndex = max1, value, i
			} else if value > max2 {
				max2 = value
			}
		}
		rootValue := combine(min1, max1, len(graph[u]), baseTime[u])
		if rootValue < answer {
			answer = rootValue
		}
		for i, edge := range graph[u] {
			if edge.to == parent[u] {
				continue
			}
			if len(graph[u]) == 1 {
				incoming[edge.to][edge.reverse] = int64(baseTime[u])
				continue
			}
			minimum, maximum := min1, max1
			if i == minIndex {
				minimum = min2
			}
			if i == maxIndex {
				maximum = max2
			}
			incoming[edge.to][edge.reverse] = combine(minimum, maximum, len(graph[u])-1, baseTime[u])
		}
	}
	return answer
}