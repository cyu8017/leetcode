// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

class Solution {
    func maxSumRangeQuery(_ nums: [Int], _ requests: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        var diff = Array(repeating: 0, count: nums.count + 1)
        for r in requests {
            diff[r[0]] += 1
            diff[r[1] + 1] -= 1
        }
        for i in 1..<nums.count { diff[i] += diff[i - 1] }
        let a = nums.sorted()
        let b = Array(diff.dropLast()).sorted()
        var ans = 0
        for i in 0..<a.count {
            ans = (ans + a[i] * b[i]) % MOD
        }
        return ans
    }
}
