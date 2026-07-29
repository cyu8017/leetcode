// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

class Solution {
    func numDupDigitsAtMostN(_ n: Int) -> Int {
        let digits = String(n).compactMap { $0.wholeNumberValue }
        let m = digits.count
        func p(_ a: Int, _ b: Int) -> Int {
            var res = 1
            for i in 0..<b { res *= a - i }
            return res
        }
        var totalUnique = 0
        for length in 1..<m {
            totalUnique += 9 * p(9, length - 1)
        }
        var used = Set<Int>()
        var broken = false
        for (i, d) in digits.enumerated() {
            let start = i == 0 ? 1 : 0
            for x in start..<d {
                if used.contains(x) { continue }
                totalUnique += p(9 - i, m - i - 1)
            }
            if used.contains(d) {
                broken = true
                break
            }
            used.insert(d)
        }
        if !broken { totalUnique += 1 }
        return n - totalUnique
    }
}
