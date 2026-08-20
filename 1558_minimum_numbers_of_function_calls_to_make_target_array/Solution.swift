// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let adds = nums.reduce(0) { $0 + $1.nonzeroBitCount }
        let shifts = nums.map { x -> Int in
            if x == 0 { return 0 }
            return Int.bitWidth - x.leadingZeroBitCount - 1
        }.max() ?? 0
        return adds + shifts
    }
}
