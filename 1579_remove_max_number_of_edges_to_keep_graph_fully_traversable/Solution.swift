// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class DSU {
    private var parent: [Int]
    var components: Int
    init(_ n: Int) {
        parent = Array(0...n)
        components = n
    }
    func find(_ x: Int) -> Int {
        var x = x
        while x != parent[x] {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }
    func union(_ a: Int, _ b: Int) -> Bool {
        var a = find(a), b = find(b)
        if a == b { return false }
        parent[a] = b
        components -= 1
        return true
    }
}

class Solution {
    func maxNumEdgesToRemove(_ n: Int, _ edges: [[Int]]) -> Int {
        let alice = DSU(n), bob = DSU(n)
        var used = 0
        for e in edges where e[0] == 3 {
            let merged = alice.union(e[1], e[2])
            _ = bob.union(e[1], e[2])
            if merged { used += 1 }
        }
        for e in edges {
            if e[0] == 1 {
                if alice.union(e[1], e[2]) { used += 1 }
            } else if e[0] == 2 {
                if bob.union(e[1], e[2]) { used += 1 }
            }
        }
        return alice.components == 1 && bob.components == 1 ? edges.count - used : -1
    }
}
