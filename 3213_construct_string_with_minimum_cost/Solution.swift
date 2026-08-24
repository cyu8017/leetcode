// LeetCode 3213 - Construct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/

class Solution {
    func minimumCost(_ target: String, _ words: [String], _ costs: [Int]) -> Int {
        let bas: Int = 13331, mod: Int = 998244353
        let inf = Int.max / 2
        let chars = Array(target)
        let n = chars.count
        var p = Array(repeating: 0, count: n + 1)
        var h = Array(repeating: 0, count: n + 1)
        p[0] = 1
        for i in 1...n {
            p[i] = p[i - 1] * bas % mod
            h[i] = (h[i - 1] * bas + Int(chars[i - 1].asciiValue!)) % mod
        }
        func query(_ l: Int, _ r: Int) -> Int {
            (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod
        }
        var f = Array(repeating: inf, count: n + 1)
        f[0] = 0
        var ss = Set<Int>()
        for w in words { ss.insert(w.count) }
        let lengths = ss.sorted()
        var d: [Int: Int] = [:]
        for i in 0..<words.count {
            var x = 0
            for c in words[i] { x = (x * bas + Int(c.asciiValue!)) % mod }
            if d[x] == nil || costs[i] < d[x]! { d[x] = costs[i] }
        }
        for i in 1...n {
            for j in lengths {
                if j > i { break }
                let x = query(i - j + 1, i)
                if let c = d[x] { f[i] = min(f[i], f[i - j] + c) }
            }
        }
        return f[n] >= inf ? -1 : f[n]
    }
}
