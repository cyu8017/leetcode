// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

func maxSubtreeInversionSum(edges [][]int, nums []int, k int) int64 {
	n := len(nums)
	graph := make([][]int, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], edge[1])
		graph[edge[1]] = append(graph[edge[1]], edge[0])
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range graph[u] {
			if parent[v] == -2 {
				parent[v] = u
				order = append(order, v)
			}
		}
	}
	const infinity int64 = 1 << 60
	maximum := make([][]int64, n)
	minimum := make([][]int64, n)
	for oi := n - 1; oi >= 0; oi-- {
		u := order[oi]
		currentMax, currentMin := make([]int64, k+1), make([]int64, k+1)
		for d := 0; d <= k; d++ {
			currentMax[d], currentMin[d] = -infinity, infinity
		}
		currentMax[k], currentMin[k] = int64(nums[u]), int64(nums[u])
		for _, v := range graph[u] {
			if parent[v] != u {
				continue
			}
			nextMax, nextMin := make([]int64, k+1), make([]int64, k+1)
			for d := 0; d <= k; d++ {
				nextMax[d], nextMin[d] = -infinity, infinity
			}
			for first := 0; first <= k; first++ {
				if currentMax[first] == -infinity {
					continue
				}
				for childDistance := 0; childDistance <= k; childDistance++ {
					if maximum[v][childDistance] == -infinity {
						continue
					}
					second := childDistance + 1
					if second > k {
						second = k
					}
					if first < k && second < k && first+second < k {
						continue
					}
					distance := first
					if second < distance {
						distance = second
					}
					maxValue := currentMax[first] + maximum[v][childDistance]
					minValue := currentMin[first] + minimum[v][childDistance]
					if maxValue > nextMax[distance] {
						nextMax[distance] = maxValue
					}
					if minValue < nextMin[distance] {
						nextMin[distance] = minValue
					}
				}
			}
			currentMax, currentMin = nextMax, nextMin
		}
		if -currentMin[k] > currentMax[0] {
			currentMax[0] = -currentMin[k]
		}
		if -currentMax[k] < currentMin[0] {
			currentMin[0] = -currentMax[k]
		}
		maximum[u], minimum[u] = currentMax, currentMin
	}
	answer := int64(-1 << 60)
	for _, value := range maximum[0] {
		if value > answer {
			answer = value
		}
	}
	return answer
}