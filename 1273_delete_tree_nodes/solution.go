// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

func deleteTreeNodes(nodes int, parent []int, value []int) int {
	children := make([][]int, nodes)
	for node := 1; node < nodes; node++ {
		children[parent[node]] = append(children[parent[node]], node)
	}
	var dfs func(int) (int, int)
	dfs = func(node int) (int, int) {
		total, count := value[node], 1
		for _, child := range children[node] {
			cs, cc := dfs(child)
			total += cs
			count += cc
		}
		if total == 0 {
			return 0, 0
		}
		return total, count
	}
	_, count := dfs(0)
	return count
}
