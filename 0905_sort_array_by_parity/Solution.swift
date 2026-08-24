// LeetCode 0905 - Sort Array By Parity
// https://leetcode.com/problems/sort-array-by-parity/

class Solution {
    func sortArrayByParity(_ nums: [Int]) -> [Int] {
        var nums = nums
        var i = 0
        for j in 0..<nums.count where nums[j] % 2 == 0 {
            nums.swapAt(i, j)
            i += 1
        }
        return nums
    }
}
