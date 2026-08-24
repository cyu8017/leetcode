// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

class Solution {
    func commonFactors(_ a: Int, _ b: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        let g = gcd(a, b)
        var ans = 0
        var i = 1
        while i * i <= g {
            if g % i == 0 {
                ans += 1
                if i * i != g { ans += 1 }
            }
            i += 1
        }
        return ans
    }
}
