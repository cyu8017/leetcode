// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

class Solution {
    func simplifiedFractions(_ n: Int) -> [String] {
        func gcd(_ a: Int, _ b: Int) -> Int { b == 0 ? a : gcd(b, a % b) }
        var ans = [String]()
        for a in 1..<n {
            for b in (a + 1)...n where gcd(a, b) == 1 {
                ans.append("\(a)/\(b)")
            }
        }
        return ans
    }
}
