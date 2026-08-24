// LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

class Solution {
    func countNonDecreasingSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var cost = 0
            var maxV = nums[i]
            for j in i..<n {
                if nums[j] >= maxV { maxV = nums[j] }
                else { cost += maxV - nums[j] }
                if cost > k { break }
                ans += 1
            }
        }
        return ans
    }
}
