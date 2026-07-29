// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
    func gcdOfStrings(_ str1: String, _ str2: String) -> String {
        if str1 + str2 != str2 + str1 {
            return ""
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        let g = gcd(str1.count, str2.count)
        return String(str1.prefix(g))
    }
}
