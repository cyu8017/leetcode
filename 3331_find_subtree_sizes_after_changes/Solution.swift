// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution {
    func findSubtreeSizes(_ parent: [Int], _ s: String) -> [Int] {
        let chars = Array(s)
        let n = parent.count
        var g = Array(repeating: [Int](), count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        var newParent = parent
        var last = Array(repeating: -1, count: 26)
        func dfs1(_ u: Int) {
            let c = Int(chars[u].asciiValue! - 97)
            let prev = last[c]
            if prev != -1 { newParent[u] = prev }
            last[c] = u
            for v in g[u] { dfs1(v) }
            last[c] = prev
        }
        dfs1(0)
        var ng = Array(repeating: [Int](), count: n)
        for i in 1..<n { ng[newParent[i]].append(i) }
        var ans = Array(repeating: 0, count: n)
        func dfs2(_ u: Int) -> Int {
            var sz = 1
            for v in ng[u] { sz += dfs2(v) }
            ans[u] = sz
            return sz
        }
        _ = dfs2(0)
        return ans
    }
}
