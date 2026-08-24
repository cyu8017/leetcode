// LeetCode 2827 - Number of Beautiful Integers in the Range
// https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

class Solution {
    func numberOfBeautifulIntegers(_ low: Int, _ high: Int, _ k: Int) -> Int {
        count(high, k) - count(low - 1, k)
    }

    private func count(_ n: Int, _ k: Int) -> Int {
        if n < 0 { return 0 }
        let s = Array(String(n))
        var memo = Array(repeating: Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: 2), count: 2), count: 22), count: 45), count: 12)
        return dfs(s, k, 0, 0, 0, 1, 0, &memo)
    }

    private func dfs(_ s: [Character], _ k: Int, _ pos: Int, _ diff: Int, _ mod: Int, _ tight: Int, _ started: Int, _ memo: inout [[[[[Int]]]]]) -> Int {
        if pos == s.count { return started == 1 && diff == 0 && mod == 0 ? 1 : 0 }
        if memo[pos][diff + 20][mod][tight][started] != -1 {
            return memo[pos][diff + 20][mod][tight][started]
        }
        let up = tight == 1 ? Int(String(s[pos]))! : 9
        var ans = 0
        for digit in 0...up {
            let nt = (tight == 1 && digit == up) ? 1 : 0
            if started == 0 {
                if digit == 0 {
                    ans += dfs(s, k, pos + 1, diff, mod, nt, 0, &memo)
                } else {
                    let nd = diff + (digit % 2 == 0 ? 1 : -1)
                    ans += dfs(s, k, pos + 1, nd, digit % k, nt, 1, &memo)
                }
            } else {
                let nd = diff + (digit % 2 == 0 ? 1 : -1)
                ans += dfs(s, k, pos + 1, nd, (mod * 10 + digit) % k, nt, 1, &memo)
            }
        }
        memo[pos][diff + 20][mod][tight][started] = ans
        return ans
    }
}
