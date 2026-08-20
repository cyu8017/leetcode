// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

class Solution {
    func kthSmallestSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        func count(_ limit: Int) -> Int {
            var total = 0, left = 0, ans = 0
            for (right, value) in nums.enumerated() {
                total += value
                while total > limit {
                    total -= nums[left]
                    left += 1
                }
                ans += right - left + 1
            }
            return ans
        }
        var lo = nums.min()!, hi = nums.reduce(0, +)
        while lo < hi {
            let mid = (lo + hi) / 2
            if count(mid) >= k { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }
}
