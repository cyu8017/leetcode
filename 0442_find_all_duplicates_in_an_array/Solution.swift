// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution {
    func findDuplicates(_ nums: [Int]) -> [Int] {
        var nums = nums
        var result: [Int] = []
        for number in nums {
            let index = abs(number) - 1
            if nums[index] < 0 {
                result.append(abs(number))
            } else {
                nums[index] = -nums[index]
            }
        }
        return result
    }
}
