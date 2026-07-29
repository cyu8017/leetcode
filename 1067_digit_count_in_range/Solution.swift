// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

class Solution {
    func digitsCount(_ d: Int, _ low: Int, _ high: Int) -> Int {
        func countUpto(_ n: Int) -> Int {
            if n < 0 { return 0 }
            let s = Array(String(n))
            let length = s.count
            var ans = 0
            for i in 0..<length {
                let left = i > 0 ? Int(String(s[0..<i]))! : 0
                let right = i + 1 < length ? Int(String(s[(i + 1)..<length]))! : 0
                let digit = Int(String(s[i]))!
                var power = 1
                for _ in 0..<(length - i - 1) { power *= 10 }
                if d != 0 {
                    ans += left * power
                    if digit > d {
                        ans += power
                    } else if digit == d {
                        ans += right + 1
                    }
                } else {
                    if i == 0 { continue }
                    ans += (left - 1) * power
                    if digit > 0 {
                        ans += power
                    } else {
                        ans += right + 1
                    }
                }
            }
            return ans
        }
        return countUpto(high) - countUpto(low - 1)
    }
}
