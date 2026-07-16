// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution {
    func findDisappearedNumbers(_ nums: [Int]) -> [Int] {
        var nums = nums
        for number in nums {
            let index = abs(number) - 1
            if nums[index] > 0 {
                nums[index] = -nums[index]
            }
        }
        var result: [Int] = []
        for (index, value) in nums.enumerated() where value > 0 {
            result.append(index + 1)
        }
        return result
    }
}
