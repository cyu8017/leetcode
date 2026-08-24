// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution {
    func kthPalindrome(_ queries: [Int], _ intLength: Int) -> [Int] {
        let half = (intLength + 1) / 2
        var start = 1
        if half > 1 {
            for _ in 1..<half { start *= 10 }
        }
        let total = start * 9
        return queries.map { q in
            if q > total { return -1 }
            var left = start + q - 1
            var pal = left
            var x = left
            if intLength % 2 != 0 { x /= 10 }
            while x > 0 {
                pal = pal * 10 + x % 10
                x /= 10
            }
            return pal
        }
    }
}
