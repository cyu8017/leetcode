// LeetCode 3327 - Check if DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

class Solution {
    func findAnswer(_ parent: [Int], _ s: String) -> [Bool] {
        let chars = Array(s)
        let n = parent.count
        var g = Array(repeating: [Int](), count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        var ans = Array(repeating: false, count: n)
        func isPal(_ t: [Character]) -> Bool {
            var i = 0, j = t.count - 1
            while i < j {
                if t[i] != t[j] { return false }
                i += 1; j -= 1
            }
            return true
        }
        func dfsStr(_ u: Int) -> [Character] {
            var out = [Character]()
            for v in g[u] { out.append(contentsOf: dfsStr(v)) }
            out.append(chars[u])
            ans[u] = isPal(out)
            return out
        }
        _ = dfsStr(0)
        return ans
    }
}
