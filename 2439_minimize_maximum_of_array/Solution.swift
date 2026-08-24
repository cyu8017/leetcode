// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
    func minimizeArrayValue(_ nums: [Int]) -> Int {
        var sum = 0
        var ans = 0
        for i in 0..<nums.count {
            sum += nums[i]
            let avg = (sum + i) / (i + 1)
            if avg > ans { ans = avg }
        }
        return ans
    }
}
