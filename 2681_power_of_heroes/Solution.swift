// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

class Solution {
    func sumOfPower(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let nums = nums.sorted()
        var ans = 0
        var s = 0
        for x in nums {
            ans = (ans + (s + x) % MOD * x % MOD * x) % MOD
            s = (s * 2 + x) % MOD
        }
        return ans
    }
}
