// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        var less = 0, eq = 0
        for x in nums {
            if x < target { less += 1 }
            else if x == target { eq += 1 }
        }
        return Array(less..<(less + eq))
    }
}
