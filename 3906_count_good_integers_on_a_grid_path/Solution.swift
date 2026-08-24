// LeetCode 3906 - Count Good Integers On A Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/

class Solution {
    private var key = [Bool](repeating: false, count: 16)
    private var s = [Character]()
    private var f = Array(repeating: [Int](repeating: -1, count: 10), count: 16)

    func countGoodIntegersOnPath(_ l: Int, _ r: Int, _ directions: String) -> Int {
        key = [Bool](repeating: false, count: 16)
        var row = 0, col = 0
        key[0] = true
        for c in directions {
            if c == "D" { row += 1 } else { col += 1 }
            key[row * 4 + col] = true
        }
        return calc(r) - calc(l - 1)
    }

    private func dfs(_ pos: Int, _ last: Int, _ lim: Bool) -> Int {
        if pos == 16 { return 1 }
        if !lim && f[pos][last] != -1 { return f[pos][last] }
        var res = 0
        let start = key[pos] ? last : 0
        let end = lim ? Int(s[pos].asciiValue! - 48) : 9
        if start <= end {
            for i in start...end {
                let nextLast = key[pos] ? i : last
                res += dfs(pos + 1, nextLast, lim && (i == end))
            }
        }
        if !lim { f[pos][last] = res }
        return res
    }

    private func calc(_ x: Int) -> Int {
        if x < 0 { return 0 }
        let t = String(x)
        s = Array(String(repeating: "0", count: 16 - t.count) + t)
        f = Array(repeating: [Int](repeating: -1, count: 10), count: 16)
        return dfs(0, 0, true)
    }
}
