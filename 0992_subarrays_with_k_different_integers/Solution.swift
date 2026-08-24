// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution {
    func subarraysWithKDistinct(_ nums: [Int], _ k: Int) -> Int {
        return atMost(nums, k) - atMost(nums, k - 1)
    }

    private func atMost(_ nums: [Int], _ m: Int) -> Int {
        if m < 0 { return 0 }
        var count = [Int: Int]()
        var left = 0, ans = 0
        for right in 0..<nums.count {
            count[nums[right], default: 0] += 1
            while count.count > m {
                let v = nums[left]
                left += 1
                count[v]! -= 1
                if count[v] == 0 { count.removeValue(forKey: v) }
            }
            ans += right - left + 1
        }
        return ans
    }
}
