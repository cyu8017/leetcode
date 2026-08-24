// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution {
    func reverseDegree(_ s: String) -> Int {
        var ans = 0
        for (i, c) in s.enumerated() {
            ans += (26 - Int(c.asciiValue! - 97)) * (i + 1)
        }
        return ans
    }
}
