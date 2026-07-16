// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

class Solution {
    func largestPalindrome(_ n: Int) -> Int {
        if n == 1 { return 9 }
        let upper = Int(pow(10.0, Double(n))) - 1
        let lower = Int(pow(10.0, Double(n - 1)))
        var first = upper
        while first >= lower {
            let reversed = String(String(first).reversed())
            let candidate = Int("\(first)\(reversed)")!
            var factor = upper
            while factor * factor >= candidate {
                if candidate % factor == 0 {
                    let partner = candidate / factor
                    if partner >= lower && partner <= upper {
                        return candidate % 1337
                    }
                }
                factor -= 1
            }
            first -= 1
        }
        return 0
    }
}
