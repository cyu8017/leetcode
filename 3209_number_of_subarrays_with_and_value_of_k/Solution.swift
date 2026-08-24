// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

class Solution {
    func countSubarrays(_ nums: [Int], _ k: Int) -> Int {
        var pre: [Int: Int] = [:]
        var ans = 0
        for x in nums {
            var cur: [Int: Int] = [:]
            for (key, val) in pre { cur[x & key, default: 0] += val }
            cur[x, default: 0] += 1
            ans += cur[k, default: 0]
            pre = cur
        }
        return ans
    }
}
