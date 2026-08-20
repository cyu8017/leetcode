// LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
// https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

class Solution {
    func minNumberOperations(_ target: [Int]) -> Int {
        var ans = target[0]
        for i in 1..<target.count {
            ans += max(0, target[i] - target[i - 1])
        }
        return ans
    }
}
