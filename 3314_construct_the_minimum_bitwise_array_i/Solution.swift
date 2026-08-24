// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: -1, count: nums.count)
        for i in 0..<nums.count {
            let n = nums[i]
            if n == 2 { continue }
            var x = 0
            while x < n {
                if (x | (x + 1)) == n { ans[i] = x; break }
                x += 1
            }
        }
        return ans
    }
}
