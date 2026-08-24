// LeetCode 3869 - Count Fancy Numbers In A Range
// https://leetcode.com/problems/count-fancy-numbers-in-a-range/

class Solution {
    private var num = [Character]()
    private var f = [[[[Int]]]]()
    private var n = 0

    private func check(_ s: Int) -> Bool {
        if s < 100 { return s % 11 != 0 }
        let mid = (s / 10) % 10
        let last = s % 10
        return mid > 1 && mid < last
    }

    func countFancy(_ l: Int, _ r: Int) -> Int {
        return calc(r) - calc(l - 1)
    }

    private func calc(_ x: Int) -> Int {
        num = Array(String(x))
        n = num.count
        f = Array(repeating: Array(repeating: Array(repeating: [Int](repeating: -1, count: 4), count: 10), count: 9 * n + 1), count: n)
        return dfs(0, 0, 0, 0, true)
    }

    private func dfs(_ pos: Int, _ s: Int, _ prev: Int, _ st: Int, _ lim: Bool) -> Int {
        if pos >= n {
            if st != 3 { return 1 }
            return check(s) ? 1 : 0
        }
        if !lim && f[pos][s][prev][st] != -1 { return f[pos][s][prev][st] }
        let up = lim ? Int(num[pos].asciiValue! - 48) : 9
        var res = 0
        for i in 0...up {
            var nxtSt = st
            if st == 0 {
                if prev == 0 { nxtSt = 0 }
                else if i > prev { nxtSt = 1 }
                else if i < prev { nxtSt = 2 }
                else { nxtSt = 3 }
            } else if st == 1 {
                nxtSt = i > prev ? 1 : 3
            } else if st == 2 {
                nxtSt = i < prev ? 2 : 3
            } else {
                nxtSt = 3
            }
            res += dfs(pos + 1, s + i, i, nxtSt, lim && i == up)
        }
        if !lim { f[pos][s][prev][st] = res }
        return res
    }
}
