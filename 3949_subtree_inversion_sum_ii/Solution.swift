// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/


class Solution {
    func maxSubtreeInversionSum(_ edges: [[Int]], _ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var graph = Array(repeating: [Int](), count: n)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        var parent = Array(repeating: -2, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in graph[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    order.append(v)
                }
            }
            i += 1
        }
        let infinity = Int.max / 4
        var maximum = Array(repeating: [Int](), count: n)
        var minimum = Array(repeating: [Int](), count: n)
        for oi in stride(from: n - 1, through: 0, by: -1) {
            let u = order[oi]
            var currentMax = Array(repeating: -infinity, count: k + 1)
            var currentMin = Array(repeating: infinity, count: k + 1)
            currentMax[k] = nums[u]
            currentMin[k] = nums[u]
            for v in graph[u] {
                if parent[v] != u { continue }
                var nextMax = Array(repeating: -infinity, count: k + 1)
                var nextMin = Array(repeating: infinity, count: k + 1)
                for first in 0...k {
                    if currentMax[first] == -infinity { continue }
                    for childDistance in 0...k {
                        if maximum[v][childDistance] == -infinity { continue }
                        var second = childDistance + 1
                        if second > k { second = k }
                        if first < k && second < k && first + second < k { continue }
                        let distance = min(first, second)
                        let maxValue = currentMax[first] + maximum[v][childDistance]
                        let minValue = currentMin[first] + minimum[v][childDistance]
                        nextMax[distance] = max(nextMax[distance], maxValue)
                        nextMin[distance] = min(nextMin[distance], minValue)
                    }
                }
                currentMax = nextMax
                currentMin = nextMin
            }
            if -currentMin[k] > currentMax[0] { currentMax[0] = -currentMin[k] }
            if -currentMax[k] < currentMin[0] { currentMin[0] = -currentMax[k] }
            maximum[u] = currentMax
            minimum[u] = currentMin
        }
        var answer = -infinity
        for value in maximum[0] { answer = max(answer, value) }
        return answer
    }
}
