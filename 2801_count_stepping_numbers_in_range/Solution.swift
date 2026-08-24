// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

class Solution {
    private let MOD = 1_000_000_007

    func countSteppingNumbers(_ low: String, _ high: String) -> Int {
        var ans = (countTo(high) - countTo(dec(low))) % MOD
        if ans < 0 { ans += MOD }
        return ans
    }

    private func countTo(_ s: String) -> Int {
        var memo = Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: 2), count: 11), count: 2), count: 85)
        return dfs(Array(s), 0, 1, -1, 0, &memo)
    }

    private func dfs(_ s: [Character], _ pos: Int, _ tight: Int, _ last: Int, _ started: Int, _ memo: inout [[[[Int]]]]) -> Int {
        if pos == s.count { return started }
        if memo[pos][tight][last + 1][started] != -1 { return memo[pos][tight][last + 1][started] }
        let up = tight == 1 ? Int(String(s[pos]))! : 9
        var ans = 0
        for d in 0...up {
            let nt = (tight == 1 && d == up) ? 1 : 0
            if started == 0 {
                ans += d == 0 ? dfs(s, pos + 1, nt, -1, 0, &memo) : dfs(s, pos + 1, nt, d, 1, &memo)
            } else if abs(d - last) == 1 {
                ans += dfs(s, pos + 1, nt, d, 1, &memo)
            }
            ans %= MOD
        }
        memo[pos][tight][last + 1][started] = ans
        return ans
    }

    private func dec(_ s: String) -> String {
        var arr = Array(s)
        var i = arr.count - 1
        while i >= 0 && arr[i] == "0" {
            arr[i] = "9"
            i -= 1
        }
        if i >= 0 {
            let v = Int(arr[i].asciiValue!) - 1
            arr[i] = Character(UnicodeScalar(v)!)
        }
        var j = 0
        while j < arr.count - 1 && arr[j] == "0" { j += 1 }
        return String(arr[j...])
    }
}
