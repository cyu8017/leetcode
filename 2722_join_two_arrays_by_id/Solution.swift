// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

class Solution {
    func join(_ arr1: [[String: Int]], _ arr2: [[String: Int]]) -> [[String: Int]] {
        var byId: [Int: [String: Int]] = [:]
        merge(&byId, arr1)
        merge(&byId, arr2)
        return byId.keys.sorted().compactMap { byId[$0] }
    }

    private func merge(_ byId: inout [Int: [String: Int]], _ arr: [[String: Int]]) {
        for obj in arr {
            guard let id = obj["id"] else { continue }
            var dest = byId[id] ?? [:]
            for (k, v) in obj { dest[k] = v }
            byId[id] = dest
        }
    }
}
