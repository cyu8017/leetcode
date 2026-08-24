// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

class Solution {
    func numberGame(_ nums: [Int]) -> [Int] {
        var nums = nums.sorted()
        var i = 0
        while i + 1 < nums.count {
            nums.swapAt(i, i + 1)
            i += 2
        }
        return nums
    }
}
