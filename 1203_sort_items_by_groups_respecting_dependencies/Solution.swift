// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution {
    func sortItems(_ n: Int, _ m: Int, _ group: [Int], _ beforeItems: [[Int]]) -> [Int] {
        var group = group
        var g = m
        for i in 0..<n where group[i] == -1 {
            group[i] = g
            g += 1
        }
        var itemGraph = [[Int]](repeating: [], count: n)
        var itemInd = [Int](repeating: 0, count: n)
        var groupGraph = [[Int]](repeating: [], count: g)
        var groupInd = [Int](repeating: 0, count: g)
        for i in 0..<n {
            for pre in beforeItems[i] {
                itemGraph[pre].append(i)
                itemInd[i] += 1
                if group[pre] != group[i] {
                    groupGraph[group[pre]].append(group[i])
                    groupInd[group[i]] += 1
                }
            }
        }
        func topo(_ graph: [[Int]], _ indeg: [Int]) -> [Int] {
            var indeg = indeg
            var q: [Int] = []
            for i in 0..<indeg.count where indeg[i] == 0 { q.append(i) }
            var order: [Int] = []
            var qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                order.append(u)
                for v in graph[u] {
                    indeg[v] -= 1
                    if indeg[v] == 0 { q.append(v) }
                }
            }
            return order.count == graph.count ? order : []
        }
        let itemOrder = topo(itemGraph, itemInd)
        let groupOrder = topo(groupGraph, groupInd)
        if itemOrder.isEmpty || groupOrder.isEmpty { return [] }
        var itemsInGroup: [Int: [Int]] = [:]
        for item in itemOrder {
            itemsInGroup[group[item], default: []].append(item)
        }
        var ans: [Int] = []
        for gi in groupOrder {
            ans.append(contentsOf: itemsInGroup[gi] ?? [])
        }
        return ans
    }
}
