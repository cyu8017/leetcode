// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

class Solution {
    func firstMissingPositive(_ nums: inout [Int]) -> Int {
        let n = nums.count
        var i = 0

        while i < n {
            let value = nums[i]
            let target = value - 1
            if value >= 1 && value <= n && nums[target] != value {
                nums.swapAt(i, target)
            } else {
                i += 1
            }
        }

        for index in 0..<n {
            if nums[index] != index + 1 {
                return index + 1
            }
        }

        return n + 1
    }
}
