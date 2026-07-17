// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

func restoreArray(adjacentPairs [][]int) []int {
    graph := make(map[int][]int)
    for _, pair := range adjacentPairs {
        a, b := pair[0], pair[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }
    start := 0
    for node, neighbors := range graph {
        if len(neighbors) == 1 {
            start = node
            break
        }
    }
    ans := []int{start}
    hasPrev := false
    prev := 0
    for len(ans) < len(graph) {
        cur := ans[len(ans)-1]
        neighbors := graph[cur]
        var nxt int
        if !hasPrev || neighbors[0] != prev {
            nxt = neighbors[0]
        } else {
            nxt = neighbors[1]
        }
        ans = append(ans, nxt)
        prev = cur
        hasPrev = true
    }
    return ans
}
