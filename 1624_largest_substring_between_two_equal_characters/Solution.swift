// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution {
    func maxLengthBetweenEqualCharacters(_ s: String) -> Int {
        var first = [Character: Int]()
        var ans = -1
        for (i, ch) in s.enumerated() {
            if let f = first[ch] {
                ans = max(ans, i - f - 1)
            } else {
                first[ch] = i
            }
        }
        return ans
    }
}
