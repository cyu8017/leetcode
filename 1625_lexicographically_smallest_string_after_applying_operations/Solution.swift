// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution {
    func findLexSmallestString(_ s: String, _ a: Int, _ b: Int) -> String {
        var seen: Set<String> = [s]
        var q = [s]
        var ans = s
        var qi = 0
        while qi < q.count {
            let cur = q[qi]; qi += 1
            if cur < ans { ans = cur }
            let chars = Array(cur)
            let add = String(chars.enumerated().map { i, ch in
                let d = Int(String(ch))!
                return Character(String(i % 2 == 1 ? (d + a) % 10 : d))
            })
            let rot = String(chars.suffix(b) + chars.prefix(chars.count - b))
            for nxt in [add, rot] where !seen.contains(nxt) {
                seen.insert(nxt)
                q.append(nxt)
            }
        }
        return ans
    }
}
