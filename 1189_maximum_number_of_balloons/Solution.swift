// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    func maxNumberOfBalloons(_ text: String) -> Int {
        var count = [Int](repeating: 0, count: 26)
        for c in text { count[Int(c.asciiValue! - 97)] += 1 }
        return min(count[1], count[0], count[11] / 2, count[14] / 2, count[13])
    }
}
