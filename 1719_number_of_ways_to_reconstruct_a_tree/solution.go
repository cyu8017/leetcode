// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

func checkWays(pairs [][]int) int {
    graph := make(map[int]map[int]bool)
    for _, pair := range pairs {
        a, b := pair[0], pair[1]
        if graph[a] == nil {
            graph[a] = make(map[int]bool)
        }
        if graph[b] == nil {
            graph[b] = make(map[int]bool)
        }
        graph[a][b] = true
        graph[b][a] = true
    }
    n := len(graph)
    root := -1
    for node, neighbors := range graph {
        if len(neighbors) == n-1 {
            root = node
            break
        }
    }
    if root == -1 {
        return 0
    }
    ans := 1
    for node, neighbors := range graph {
        if node == root {
            continue
        }
        parent := -1
        parentDegree := n + 1
        for nei := range neighbors {
            if len(graph[nei]) >= len(neighbors) && len(graph[nei]) < parentDegree {
                parent = nei
                parentDegree = len(graph[nei])
            }
        }
        if parent == -1 {
            return 0
        }
        for nei := range neighbors {
            if nei != parent && !graph[parent][nei] {
                return 0
            }
        }
        if len(graph[parent]) == len(neighbors) {
            ans = 2
        }
    }
    return ans
}
