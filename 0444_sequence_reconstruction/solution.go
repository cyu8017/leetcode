// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

func sequenceReconstruction(nums []int, sequences [][]int) bool {
	indegree := make(map[int]int, len(nums))
	graph := make(map[int]map[int]struct{}, len(nums))
	seenEdges := make(map[[2]int]struct{})

	for _, value := range nums {
		indegree[value] = 0
		graph[value] = make(map[int]struct{})
	}

	for _, sequence := range sequences {
		for index := 0; index+1 < len(sequence); index++ {
			left := sequence[index]
			right := sequence[index+1]
			edge := [2]int{left, right}
			if _, seen := seenEdges[edge]; seen {
				continue
			}
			seenEdges[edge] = struct{}{}
			if _, exists := graph[left][right]; !exists {
				graph[left][right] = struct{}{}
				indegree[right]++
			}
		}
	}

	queue := make([]int, 0)
	for _, value := range nums {
		if indegree[value] == 0 {
			queue = append(queue, value)
		}
	}

	order := make([]int, 0, len(nums))
	for len(queue) > 0 {
		if len(queue) > 1 {
			return false
		}
		node := queue[0]
		queue = queue[1:]
		order = append(order, node)
		for neighbor := range graph[node] {
			indegree[neighbor]--
			if indegree[neighbor] == 0 {
				queue = append(queue, neighbor)
			}
		}
	}

	if len(order) != len(nums) {
		return false
	}
	for index := range nums {
		if order[index] != nums[index] {
			return false
		}
	}
	return true
}
