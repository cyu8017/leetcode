// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution {
    func numberOfGoodSubarraySplits(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var ones: [Int] = []
        for i in nums.indices where nums[i] == 1 { ones.append(i) }
        if ones.isEmpty { return 0 }
        var ans = 1
        for i in 1..<ones.count {
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        }
        return ans
    }
}
