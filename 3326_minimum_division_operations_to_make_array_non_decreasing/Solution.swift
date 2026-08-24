// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var nums = nums
        var ops = 0
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= nums[i + 1] { continue }
            while nums[i] > nums[i + 1] {
                let d = smallestProperDivisor(nums[i])
                if d == nums[i] { return -1 }
                nums[i] /= d
                ops += 1
                if nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) == nums[i] { return -1 }
            }
        }
        return ops
    }

    private func smallestProperDivisor(_ x: Int) -> Int {
        var d = 2
        while d * d <= x {
            if x % d == 0 { return d }
            d += 1
        }
        return x
    }
}
