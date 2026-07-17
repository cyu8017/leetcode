// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution {
    func countBalls(_ lowLimit: Int, _ highLimit: Int) -> Int {
        var counts: [Int: Int] = [:]
        for value in lowLimit...highLimit {
            var box = 0
            var v = value
            while v > 0 {
                box += v % 10
                v /= 10
            }
            counts[box, default: 0] += 1
        }
        return counts.values.max() ?? 0
    }
}
