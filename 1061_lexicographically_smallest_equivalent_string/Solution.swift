// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution {
    func smallestEquivalentString(_ s1: String, _ s2: String, _ baseStr: String) -> String {
        var parent = Array(0..<26)

        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }

        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra == rb { return }
            if ra < rb {
                parent[rb] = ra
            } else {
                parent[ra] = rb
            }
        }

        let a1 = Array(s1.utf8)
        let a2 = Array(s2.utf8)
        for i in 0..<a1.count {
            union(Int(a1[i]) - 97, Int(a2[i]) - 97)
        }
        return String(baseStr.utf8.map { Character(UnicodeScalar(find(Int($0) - 97) + 97)!) })
    }
}
