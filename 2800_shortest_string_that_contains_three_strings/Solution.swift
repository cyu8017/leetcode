// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    func minimumString(_ a: String, _ b: String, _ c: String) -> String {
        let perms = [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]
        var ans = ""
        for p in perms {
            let cur = merge(merge(p[0], p[1]), p[2])
            if ans.isEmpty || cur.count < ans.count || (cur.count == ans.count && cur < ans) {
                ans = cur
            }
        }
        return ans
    }

    private func merge(_ x: String, _ y: String) -> String {
        if x.contains(y) { return x }
        var best = x + y
        let n = min(x.count, y.count)
        for i in stride(from: n, through: 1, by: -1) {
            if x.suffix(i) == y.prefix(i) {
                let cand = x + String(y.dropFirst(i))
                if cand.count < best.count || (cand.count == best.count && cand < best) {
                    best = cand
                }
                break
            }
        }
        return best
    }
}
