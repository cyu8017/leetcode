// LeetCode 0902 - Numbers At Most N Given Digit Set
// https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution {
    func atMostNGivenDigitSet(_ digits: [String], _ n: Int) -> Int {
        let k = digits.count
        let s = Array(String(n))
        let m = s.count
        func ipow(_ bas: Int, _ exp: Int) -> Int {
            var r = 1, e = exp
            while e > 0 { r *= bas; e -= 1 }
            return r
        }
        func countUpTo(_ t: [Character]) -> Int {
            if t.isEmpty { return 0 }
            var first = 0
            for d in digits where d.first! < t[0] { first += 1 }
            var ways = first * ipow(k, t.count - 1)
            var found = false
            for d in digits where d.first! == t[0] { found = true; break }
            if found { ways += countUpTo(Array(t.dropFirst())) }
            return ways
        }
        var ans = 0
        if m > 1 {
            for i in 1..<m { ans += ipow(k, i) }
        }
        ans += countUpTo(s)
        return ans
    }
}
