// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution {
    func numSubarrayBoundedMax(_ nums: [Int], _ left: Int, _ right: Int) -> Int {
        return countAtMost(nums, right) - countAtMost(nums, left - 1)
    }

    private func countAtMost(_ nums: [Int], _ bound: Int) -> Int {
        var ans = 0, cur = 0
        for num in nums {
            if num <= bound {
                cur += 1
                ans += cur
            } else {
                cur = 0
            }
        }
        return ans
    }
}
