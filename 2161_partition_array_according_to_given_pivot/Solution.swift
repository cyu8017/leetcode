// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution {
    func pivotArray(_ nums: [Int], _ pivot: Int) -> [Int] {
        return nums.filter { $0 < pivot } + nums.filter { $0 == pivot } + nums.filter { $0 > pivot }
    }
}
