// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    n := len(source)
    parent := make([]int, n)
    for i := range parent {
        parent[i] = i
    }
    var find func(x int) int
    find = func(x int) int {
        for parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }
    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra != rb {
            parent[rb] = ra
        }
    }

    for _, swap := range allowedSwaps {
        union(swap[0], swap[1])
    }
    groups := make(map[int]map[int]int)
    for i, value := range source {
        root := find(i)
        if groups[root] == nil {
            groups[root] = make(map[int]int)
        }
        groups[root][value]++
    }
    ans := 0
    for i, value := range target {
        counts := groups[find(i)]
        if counts[value] > 0 {
            counts[value]--
        } else {
            ans++
        }
    }
    return ans
}
