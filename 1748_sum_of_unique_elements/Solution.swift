// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

class Solution {
    func sumOfUnique(_ nums: [Int]) -> Int {
        var counts = [Int: Int]()
        for value in nums {
            counts[value, default: 0] += 1
        }
        var total = 0
        for (value, count) in counts where count == 1 {
            total += value
        }
        return total
    }
}
