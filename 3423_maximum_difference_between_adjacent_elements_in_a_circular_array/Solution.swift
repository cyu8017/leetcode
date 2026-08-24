// LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
// https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution {
    func maxAdjacentDistance(_ nums: [Int]) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            let d = abs(nums[i] - nums[(i + 1) % n])
            if d > ans { ans = d }
        }
        return ans
    }
}
