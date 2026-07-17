// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution {
    func restoreArray(_ adjacentPairs: [[Int]]) -> [Int] {
        var graph: [Int: [Int]] = [:]
        for pair in adjacentPairs {
            graph[pair[0], default: []].append(pair[1])
            graph[pair[1], default: []].append(pair[0])
        }
        var start = 0
        outer: for pair in adjacentPairs {
            for node in pair where graph[node]!.count == 1 {
                start = node
                break outer
            }
        }
        let n = graph.count
        var ans = [start]
        ans.reserveCapacity(n)
        var prev: Int? = nil
        while ans.count < n {
            let cur = ans[ans.count - 1]
            let neighbors = graph[cur]!
            let nxt = neighbors[0] != prev ? neighbors[0] : neighbors[1]
            ans.append(nxt)
            prev = cur
        }
        return ans
    }
}
