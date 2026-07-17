// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution {
    func minOperations(_ boxes: String) -> [Int] {
        let digits = boxes.map { $0 == "1" ? 1 : 0 }
        let n = digits.count
        var ans = [Int](repeating: 0, count: n)
        var balls = 0
        var ops = 0
        if n > 1 {
            for i in 1..<n {
                balls += digits[i - 1]
                ops += balls
                ans[i] = ops
            }
            balls = 0
            ops = 0
            for i in stride(from: n - 2, through: 0, by: -1) {
                balls += digits[i + 1]
                ops += balls
                ans[i] += ops
            }
        }
        return ans
    }
}
