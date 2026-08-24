// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

class Solution {
    func minimumOperations(_ nums: [Int], _ target: [Int]) -> Int {
        var f = abs(target[0] - nums[0])
        for i in 1..<target.count {
            let x = target[i] - nums[i]
            let y = target[i - 1] - nums[i - 1]
            if x * y > 0 {
                let d = abs(x) - abs(y)
                if d > 0 { f += d }
            } else {
                f += abs(x)
            }
        }
        return f
    }
}
