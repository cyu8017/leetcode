// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

class Solution {
    func findGoodStrings(_ n: Int, _ s1: String, _ s2: String, _ evil: String) -> Int {
        let mod = 1_000_000_007
        let e = Array(evil), m = e.count
        let a1 = Array(s1), a2 = Array(s2)
        var pi = Array(repeating: 0, count: max(m, 1))
        if m > 1 {
            for i in 1..<m {
                var j = pi[i - 1]
                while j > 0 && e[i] != e[j] { j = pi[j - 1] }
                if e[i] == e[j] { j += 1 }
                pi[i] = j
            }
        }
        var trans = Array(repeating: Array(repeating: 0, count: 26), count: max(m, 1))
        if m > 0 {
            for j in 0..<m {
                for x in 0..<26 {
                    let c = Character(UnicodeScalar(97 + x)!)
                    var k = j
                    while k > 0 && (k >= m || e[k] != c) { k = pi[k - 1] }
                    if k < m && e[k] == c { k += 1 }
                    trans[j][x] = k
                }
            }
        }
        var memo = [Int: Int]()
        func pack(_ i: Int, _ j: Int, _ lo: Bool, _ hi: Bool) -> Int {
            return (((i * 51 + j) * 2 + (lo ? 1 : 0)) * 2) + (hi ? 1 : 0)
        }
        func dp(_ i: Int, _ j: Int, _ lo: Bool, _ hi: Bool) -> Int {
            if j == m { return 0 }
            if i == n { return 1 }
            let key = pack(i, j, lo, hi)
            if let v = memo[key] { return v }
            let a = lo ? Int(a1[i].asciiValue!) - 97 : 0
            let b = hi ? Int(a2[i].asciiValue!) - 97 : 25
            var ans = 0
            for x in a...b {
                let nj = m == 0 ? 0 : trans[j][x]
                ans = (ans + dp(i + 1, nj, lo && x == a, hi && x == b)) % mod
            }
            memo[key] = ans
            return ans
        }
        return dp(0, 0, true, true)
    }
}
