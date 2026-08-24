// LeetCode 2999 - Count the Number of Powerful Integers
// https://leetcode.com/problems/count-the-number-of-powerful-integers/

class Solution {
    private var s = ""
    private var limit = 0

    func numberOfPowerfulInt(_ start: Int, _ finish: Int, _ limit: Int, _ s: String) -> Int {
        self.s = s
        self.limit = limit
        return count(finish) - count(start - 1)
    }

    private func count(_ num: Int) -> Int {
        if num < 0 { return 0 }
        for ch in s {
            if Int(String(ch))! > limit { return 0 }
        }
        let t = String(num)
        let n = t.count, sn = s.count
        if n < sn { return 0 }
        var ans = 0
        for length in sn..<n {
            let preLen = length - sn
            if preLen == 0 {
                ans += 1
            } else {
                var ways = limit
                if preLen > 1 {
                    for _ in 1..<preLen { ways *= (limit + 1) }
                }
                ans += ways
            }
        }
        let pref = n - sn
        var memo: [Int: Int] = [:]
        ans += dfs(Array(t), pref, 0, true, &memo)
        return ans
    }

    private func dfs(_ t: [Character], _ pref: Int, _ i: Int, _ tight: Bool, _ memo: inout [Int: Int]) -> Int {
        if i == pref {
            if tight {
                return String(t[pref...]) >= s ? 1 : 0
            }
            return 1
        }
        let key = (i << 1) | (tight ? 1 : 0)
        if let v = memo[key] { return v }
        var up = tight ? Int(String(t[i]))! : limit
        if up > limit { up = limit }
        var res = 0
        for d in 0...up {
            if i == 0 && d == 0 { continue }
            res += dfs(t, pref, i + 1, tight && d == Int(String(t[i]))!, &memo)
        }
        memo[key] = res
        return res
    }
}
