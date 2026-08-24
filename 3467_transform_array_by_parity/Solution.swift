// LeetCode 3467 - Transform Array by Parity
// https://leetcode.com/problems/transform-array-by-parity/

class Solution {
    func transformArray(_ nums: [Int]) -> [Int] {
        var nums = nums.map { $0 % 2 }
        var j = 0
        for i in 0..<nums.count where nums[i] == 0 {
            nums.swapAt(i, j)
            j += 1
        }
        return nums
    }
}
