// LeetCode 3032 - Count Numbers With Unique Digits II
// https://leetcode.com/problems/count-numbers-with-unique-digits-ii/

class Solution {
    private var numChars: [Character] = []
    private var f: [[Int]] = []

    func numberCount(_ a: Int, _ b: Int) -> Int {
        numChars = Array(String(b))
        reset()
        let y = dfs(0, 0, true)
        numChars = Array(String(a - 1))
        reset()
        let x = dfs(0, 0, true)
        return y - x
    }

    private func reset() {
        f = Array(repeating: Array(repeating: -1, count: 1 << 10), count: numChars.count)
    }

    private func dfs(_ pos: Int, _ mask: Int, _ limit: Bool) -> Int {
        if pos >= numChars.count { return mask != 0 ? 1 : 0 }
        if !limit && f[pos][mask] != -1 { return f[pos][mask] }
        let up = limit ? Int(String(numChars[pos]))! : 9
        var ans = 0
        for i in 0...up {
            if ((mask >> i) & 1) != 0 { continue }
            var nxt = mask | (1 << i)
            if mask == 0 && i == 0 { nxt = 0 }
            ans += dfs(pos + 1, nxt, limit && i == up)
        }
        if !limit { f[pos][mask] = ans }
        return ans
    }
}
