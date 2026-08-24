// LeetCode 2117 - Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/

class Solution {
    func abbreviateProduct(_ left: Int, _ right: Int) -> String {
        var twos = 0, fives = 0
        for i in left...right {
            var x = i
            while x % 2 == 0 { twos += 1; x /= 2 }
            while x % 5 == 0 { fives += 1; x /= 5 }
        }
        let zeros = min(twos, fives)
        let MOD = 100_000_000_000
        var prod = 1
        let extra2 = twos - zeros, extra5 = fives - zeros
        var logSum = 0.0
        for i in left...right {
            var x = i
            while x % 2 == 0 { x /= 2 }
            while x % 5 == 0 { x /= 5 }
            prod = (prod * x) % MOD
            logSum += log10(Double(x))
        }
        for _ in 0..<extra2 { prod = (prod * 2) % MOD; logSum += log10(2.0) }
        for _ in 0..<extra5 { prod = (prod * 5) % MOD; logSum += log10(5.0) }
        var fullLog = 0.0
        for i in left...right { fullLog += log10(Double(i)) }
        let digits = Int(fullLog) + 1
        if digits <= 10 {
            var p = 1
            for i in left...right { p *= i }
            return String(p)
        }
        let frac = logSum - floor(logSum)
        let prefix = Int(pow(10.0, frac + 4))
        let suffix = prod % 100000
        return String(prefix) + "e" + String(zeros) + String(format: "%05d", suffix)
    }
}
