// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/


class Solution {
    func minAdjacentSwaps(_ nums: [Int], _ a: Int, _ b: Int) -> Int {
        let MOD = 1_000_000_007
        var result = 0, cnt1 = 0, cnt2 = 0
        for x in nums {
            if x < a {
                result = (result + cnt1 + cnt2) % MOD
            } else if x <= b {
                cnt1 += 1
                result = (result + cnt2) % MOD
            } else {
                cnt2 += 1
            }
        }
        return result
    }
}
