// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

class Solution {
    func arrayPairSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var total = 0
        var i = 0
        while i < sorted.count {
            total += sorted[i]
            i += 2
        }
        return total
    }
}
