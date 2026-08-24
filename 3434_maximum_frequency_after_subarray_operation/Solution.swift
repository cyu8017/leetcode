// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int) -> Int {
        var base = 0
        for x in nums where x == k { base += 1 }
        var ans = base
        for v in Set(nums) where v != k {
            var best = 0, cur = 0
            for x in nums {
                var delta = 0
                if x == v { delta = 1 }
                else if x == k { delta = -1 }
                cur += delta
                if cur < 0 { cur = 0 }
                if cur > best { best = cur }
            }
            if base + best > ans { ans = base + best }
        }
        return ans
    }
}
