// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution {
    func largestSumAfterKNegations(_ nums: [Int], _ k: Int) -> Int {
        var nums = nums.sorted()
        var k = k
        for i in 0..<nums.count {
            if k > 0 && nums[i] < 0 {
                nums[i] = -nums[i]
                k -= 1
            }
        }
        if k % 2 == 1 {
            nums.sort()
            nums[0] = -nums[0]
        }
        return nums.reduce(0, +)
    }
}
