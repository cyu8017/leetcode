// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution {
    func bestRotation(_ nums: [Int]) -> Int {
        let n = nums.count
        var change = Array(repeating: 1, count: n)
        for i in 0..<n {
            change[(i - nums[i] + 1 + n) % n] -= 1
        }
        for i in 1..<n { change[i] += change[i - 1] }
        var best = 0
        for i in 1..<n where change[i] > change[best] { best = i }
        return best
    }
}
