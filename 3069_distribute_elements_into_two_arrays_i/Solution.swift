// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution {
    func resultArray(_ nums: [Int]) -> [Int] {
        var arr1 = [nums[0]]
        var arr2 = [nums[1]]
        for i in 2..<nums.count {
            if arr1.last! > arr2.last! {
                arr1.append(nums[i])
            } else {
                arr2.append(nums[i])
            }
        }
        return arr1 + arr2
    }
}
