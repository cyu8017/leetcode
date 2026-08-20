// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

class Solution {
    func smallestStringWithSwaps(_ s: String, _ pairs: [[Int]]) -> String {
        let chars = Array(s)
        let n = chars.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for p in pairs {
            let a = find(p[0]), b = find(p[1])
            parent[a] = b
        }
        var groups: [Int: [Character]] = [:]
        for i in 0..<n {
            groups[find(i), default: []].append(chars[i])
        }
        for k in groups.keys {
            groups[k]!.sort()
        }
        var idx: [Int: Int] = [:]
        var result = chars
        for i in 0..<n {
            let root = find(i)
            let j = idx[root, default: 0]
            result[i] = groups[root]![j]
            idx[root] = j + 1
        }
        return String(result)
    }
}
