// LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/

class Solution {
    var k = 0
    var s = [Character]()
    var memo = [String: Int]()

    func depth(_ x0: Int) -> Int {
        if x0 <= 0 { return 100 }
        var x = x0, d = 0
        while x > 1 {
            x = x.nonzeroBitCount
            d += 1
        }
        return d
    }

    func dfs(_ pos: Int, _ tight: Int, _ started: Int, _ pc: Int) -> Int {
        if pos == s.count {
            if started == 0 { return 0 }
            if pc == 1 { return k == 1 ? 1 : 0 }
            return depth(pc) == k - 1 ? 1 : 0
        }
        let key = "\(pos),\(tight),\(started),\(pc)"
        if let v = memo[key] { return v }
        let up = tight == 1 ? Int(s[pos].asciiValue! - 48) : 1
        var res = 0
        for dig in 0...up {
            let nt = (tight == 1 && dig == up) ? 1 : 0
            if started == 0 && dig == 0 { res += dfs(pos + 1, nt, 0, 0) }
            else { res += dfs(pos + 1, nt, 1, pc + dig) }
        }
        memo[key] = res
        return res
    }

    func popcountDepth(_ n: Int, _ k: Int) -> Int {
        self.k = k
        if k == 0 { return n >= 1 ? 1 : 0 }
        var bits = [Character]()
        var x = n
        while x > 0 {
            bits.append(Character(UnicodeScalar(48 + (x & 1))!))
            x >>= 1
        }
        s = Array(bits.reversed())
        if s.isEmpty { s = ["0"] }
        memo = [:]
        return dfs(0, 1, 0, 0)
    }
}
