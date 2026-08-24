// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

class Solution {
    func minOperations(_ k: Int) -> Int {
        var ans = k
        for a in 0..<k {
            let x = a + 1
            let b = (k + x - 1) / x - 1
            ans = min(ans, a + b)
        }
        return ans
    }
}
