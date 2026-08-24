// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
    func smallestValue(_ n: Int) -> Int {
        func sumPrimeFactors(_ x: Int) -> Int {
            var x = x, s = 0
            var i = 2
            while i * i <= x {
                while x % i == 0 {
                    s += i
                    x /= i
                }
                i += 1
            }
            if x > 1 { s += x }
            return s
        }
        var n = n
        while true {
            let s = sumPrimeFactors(n)
            if s == n { return n }
            n = s
        }
    }
}
