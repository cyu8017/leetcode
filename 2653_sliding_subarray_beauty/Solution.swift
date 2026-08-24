// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    func getSubarrayBeauty(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var freq = Array(repeating: 0, count: 101)
        var ans = Array(repeating: 0, count: nums.count - k + 1)
        for i in nums.indices {
            freq[nums[i] + 50] += 1
            if i >= k { freq[nums[i - k] + 50] -= 1 }
            if i >= k - 1 {
                var need = x
                var val = 0
                for j in 0..<50 {
                    need -= freq[j]
                    if need <= 0 {
                        val = j - 50
                        break
                    }
                }
                ans[i - k + 1] = val
            }
        }
        return ans
    }
}
