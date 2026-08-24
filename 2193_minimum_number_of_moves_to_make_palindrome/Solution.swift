// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution {
    func minMovesToMakePalindrome(_ s: String) -> Int {
        var b = Array(s)
        var ans = 0
        while b.count > 1 {
            var j = b.count - 1
            while j > 0 && b[j] != b[0] { j -= 1 }
            if j == 0 {
                ans += b.count / 2
                b.removeFirst()
                continue
            }
            ans += b.count - 1 - j
            b.remove(at: j)
            b.removeFirst()
        }
        return ans
    }
}
