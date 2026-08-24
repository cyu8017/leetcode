// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

class Solution {
    func mergeSimilarItems(_ items1: [[Int]], _ items2: [[Int]]) -> [[Int]] {
        var mp: [Int: Int] = [:]
        for it in items1 { mp[it[0], default: 0] += it[1] }
        for it in items2 { mp[it[0], default: 0] += it[1] }
        return mp.keys.sorted().map { [$0, mp[$0]!] }
    }
}
