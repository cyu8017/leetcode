// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

class Solution {
    func smallestRangeI(_ nums: [Int], _ k: Int) -> Int {
        return max(0, (nums.max() ?? 0) - (nums.min() ?? 0) - 2 * k)
    }
}
