// LeetCode 2460 - Apply Operations to an Array
// https://leetcode.com/problems/apply-operations-to-an-array/

class Solution {
    func applyOperations(_ nums: [Int]) -> [Int] {
        var nums = nums
        let n = nums.count
        for i in 0..<(n - 1) {
            if nums[i] == nums[i + 1] {
                nums[i] *= 2
                nums[i + 1] = 0
            }
        }
        var ans = [Int](repeating: 0, count: n)
        var j = 0
        for x in nums where x != 0 {
            ans[j] = x
            j += 1
        }
        return ans
    }
}
