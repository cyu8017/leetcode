// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution {
    func maxDistinctElements(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 0
        var prev = Int.min / 2
        for x in nums {
            var cur = x - k
            if cur <= prev { cur = prev + 1 }
            if cur > x + k { continue }
            ans += 1
            prev = cur
        }
        return ans
    }
}
