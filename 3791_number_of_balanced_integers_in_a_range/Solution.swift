// LeetCode 3791 - Number Of Balanced Integers In A Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/

class Solution {
    private let BASE = 90
    private var num = [Character]()
    private var f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)

    private func dfs(_ pos: Int, _ diff: Int, _ lim: Bool) -> Int {
        if pos >= num.count { return diff == 0 ? 1 : 0 }
        if !lim && f[pos][diff + BASE] != -1 { return f[pos][diff + BASE] }
        let up = lim ? Int(num[pos].asciiValue! - 48) : 9
        var res = 0
        for i in 0...up {
            if pos % 2 == 0 { res += dfs(pos + 1, diff + i, lim && i == up) }
            else { res += dfs(pos + 1, diff - i, lim && i == up) }
        }
        if !lim { f[pos][diff + BASE] = res }
        return res
    }

    func countBalanced(_ low: Int, _ high: Int) -> Int {
        if high < 11 { return 0 }
        var low = low
        if low < 11 { low = 11 }
        num = Array(String(low - 1))
        f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)
        let a = dfs(0, 0, true)
        num = Array(String(high))
        f = Array(repeating: [Int](repeating: -1, count: 181), count: 20)
        let b = dfs(0, 0, true)
        return b - a
    }
}
