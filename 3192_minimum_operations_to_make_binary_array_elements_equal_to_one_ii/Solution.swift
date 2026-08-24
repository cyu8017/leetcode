// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var ans = 0, v = 0
        for raw in nums {
            if (raw ^ v) == 0 {
                v ^= 1
                ans += 1
            }
        }
        return ans
    }
}
