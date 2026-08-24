// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

class Solution {
    func maximumOr(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var pref = Array(repeating: 0, count: n + 1)
        var suf = Array(repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] | nums[i] }
        for i in stride(from: n - 1, through: 0, by: -1) { suf[i] = suf[i + 1] | nums[i] }
        var ans = 0
        for i in 0..<n {
            ans = max(ans, pref[i] | (nums[i] << k) | suf[i + 1])
        }
        return ans
    }
}
