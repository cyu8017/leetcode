// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

class Solution {
    func maxSelectedElements(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var dp: [Int: Int] = [:]
        var ans = 0
        for num in nums {
            let dn = dp[num, default: 0]
            let dnm1 = dp[num - 1, default: 0]
            dp[num + 1] = dn + 1
            dp[num] = dnm1 + 1
            ans = max(ans, max(dp[num]!, dp[num + 1]!))
        }
        return ans
    }
}
