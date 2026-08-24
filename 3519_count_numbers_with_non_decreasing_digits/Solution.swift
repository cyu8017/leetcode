// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

class Solution {
    let MOD = 1_000_000_007

    func toDigits(_ s0: String, _ b: Int) -> [Int] {
        var s = s0
        if s == "0" { return [0] }
        var digs = [Int]()
        while !(s.count == 1 && s.first == "0") {
            var rem = 0
            var q = ""
            for c in s {
                let cur = rem * 10 + Int(c.asciiValue! - 48)
                let d = cur / b
                rem = cur % b
                if !q.isEmpty || d != 0 { q.append(Character(UnicodeScalar(48 + d)!)) }
            }
            digs.append(rem)
            s = q.isEmpty ? "0" : q
        }
        digs.reverse()
        return digs
    }

    func dec(_ s: String) -> String {
        var a = Array(s)
        var i = a.count - 1
        while i >= 0 && a[i] == "0" {
            a[i] = "9"
            i -= 1
        }
        if i < 0 { return "0" }
        let v = Int(String(a[i]))! - 1
        a[i] = Character(UnicodeScalar(48 + v)!)
        var t = String(a)
        while t.count > 1 && t.first == "0" { t.removeFirst() }
        return t
    }

    func countUpto(_ digs: [Int], _ b: Int) -> Int {
        let m = digs.count
        var memo = [String: Int]()
        func dfs(_ pos: Int, _ last: Int, _ tight: Bool) -> Int {
            if pos == m { return 1 }
            let key = "\(pos),\(last),\(tight ? 1 : 0)"
            if let v = memo[key] { return v }
            let up = tight ? digs[pos] : b - 1
            var res = 0
            if last <= up {
                for d in last...up {
                    res = (res + dfs(pos + 1, d, tight && d == up)) % MOD
                }
            }
            memo[key] = res
            return res
        }
        return dfs(0, 0, true)
    }

    func countNumbers(_ l: String, _ r: String, _ b: Int) -> Int {
        let rd = toDigits(r, b)
        let ld = toDigits(dec(l), b)
        return (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
    }
}
