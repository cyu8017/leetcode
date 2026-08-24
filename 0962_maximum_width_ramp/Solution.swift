// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

class Solution {
    func maxWidthRamp(_ nums: [Int]) -> Int {
        var stack = [Int]()
        for i in 0..<nums.count {
            if stack.isEmpty || nums[stack.last!] > nums[i] { stack.append(i) }
        }
        var ans = 0
        for j in stride(from: nums.count - 1, through: 0, by: -1) {
            while !stack.isEmpty && nums[stack.last!] <= nums[j] {
                ans = max(ans, j - stack.last!)
                stack.removeLast()
            }
        }
        return ans
    }
}
