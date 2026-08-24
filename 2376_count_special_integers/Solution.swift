// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

class Solution {
    func countSpecialNumbers(_ n: Int) -> Int {
        let s = Array(String(n))
        let m = s.count
        var ans = 0
        var perm = 9
        if m > 1 {
            for i in 1..<m {
                ans += perm
                perm *= (10 - i)
            }
        }
        var used = [Bool](repeating: false, count: 10)
        for i in 0..<m {
            let start = i == 0 ? 1 : 0
            let digit = Int(String(s[i]))!
            if start < digit {
                for d in start..<digit {
                    if used[d] { continue }
                    var rem = 10 - (i + 1)
                    var ways = 1
                    if i + 1 < m {
                        for _ in (i + 1)..<m {
                            ways *= rem
                            rem -= 1
                        }
                    }
                    ans += ways
                }
            }
            if used[digit] { return ans }
            used[digit] = true
        }
        return ans + 1
    }
}
