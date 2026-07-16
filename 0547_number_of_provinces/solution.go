// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)
	parent := make([]int, n)
	for index := range parent {
		parent[index] = index
	}

	var find func(node int) int
	find = func(node int) int {
		if parent[node] != node {
			parent[node] = find(parent[node])
		}
		return parent[node]
	}

	unite := func(left, right int) {
		rootLeft := find(left)
		rootRight := find(right)
		if rootLeft != rootRight {
			parent[rootRight] = rootLeft
		}
	}

	for row := 0; row < n; row++ {
		for col := row + 1; col < n; col++ {
			if isConnected[row][col] == 1 {
				unite(row, col)
			}
		}
	}

	provinces := 0
	for index := 0; index < n; index++ {
		if find(index) == index {
			provinces++
		}
	}
	return provinces
}
