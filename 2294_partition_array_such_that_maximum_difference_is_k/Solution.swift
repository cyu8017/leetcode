// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution {
    func partitionArray(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 1, start = nums[0]
        for i in 1..<nums.count {
            if nums[i] - start > k {
                ans += 1
                start = nums[i]
            }
        }
        return ans
    }
}
