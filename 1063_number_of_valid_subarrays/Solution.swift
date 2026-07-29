// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

class Solution {
    func validSubarrays(_ nums: [Int]) -> Int {
        var stack: [Int] = []
        var ans = 0
        for (i, x) in nums.enumerated() {
            while let last = stack.last, nums[last] > x {
                let j = stack.removeLast()
                ans += i - j
            }
            stack.append(i)
        }
        while let j = stack.popLast() {
            ans += nums.count - j
        }
        return ans
    }
}
