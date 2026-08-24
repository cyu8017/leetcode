// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

class Solution {
    func arrayChange(_ nums: [Int], _ operations: [[Int]]) -> [Int] {
        var nums = nums
        var pos: [Int: Int] = [:]
        for i in 0..<nums.count { pos[nums[i]] = i }
        for op in operations {
            let i = pos[op[0]]!
            nums[i] = op[1]
            pos.removeValue(forKey: op[0])
            pos[op[1]] = i
        }
        return nums
    }
}
