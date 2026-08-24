// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var sum = 0
        var hasPos = false
        var maxNeg = Int(-1e9)
        for x in nums {
            if x < 0 {
                if x > maxNeg { maxNeg = x }
                continue
            }
            hasPos = true
            if seen.insert(x).inserted { sum += x }
        }
        return hasPos ? sum : maxNeg
    }
}
