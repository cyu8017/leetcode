// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

class Solution {
    func possibleStringCount(_ word: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let w = Array(word)
        var groups = [Int]()
        var i = 0
        while i < w.count {
            var j = i
            while j < w.count && w[j] == w[i] { j += 1 }
            groups.append(j - i)
            i = j
        }
        var total = 1
        for g in groups { total = total * g % mod }
        if k <= groups.count { return total }
        let need = k - 1
        var dp = Array(repeating: 0, count: need)
        dp[0] = 1
        for g in groups {
            var ndp = Array(repeating: 0, count: need)
            var pref = Array(repeating: 0, count: need + 1)
            for i in 0..<need { pref[i + 1] = (pref[i] + dp[i]) % mod }
            for s in 0..<need {
                var lo = s - g
                if lo < 0 { lo = 0 }
                let hi = s - 1
                if hi >= 0 { ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod }
            }
            dp = ndp
        }
        var bad = 0
        for v in dp { bad = (bad + v) % mod }
        return (total - bad + mod) % mod
    }
}
