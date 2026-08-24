// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution {
    func removeStones(_ stones: [[Int]]) -> Int {
        var parent = [Int: Int]()
        func find(_ x: Int) -> Int {
            if parent[x] == nil { parent[x] = x }
            if parent[x]! != x { parent[x] = find(parent[x]!) }
            return parent[x]!
        }
        func unite(_ a: Int, _ b: Int) {
            parent[find(a)] = find(b)
        }
        for s in stones { unite(s[0], ~s[1]) }
        var roots = Set<Int>()
        for s in stones { roots.insert(find(s[0])) }
        return stones.count - roots.count
    }
}
