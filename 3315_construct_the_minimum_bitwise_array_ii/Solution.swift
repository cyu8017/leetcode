// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: -1, count: nums.count)
        for i in 0..<nums.count {
            let n = nums[i]
            if n == 2 { continue }
            for b in 0..<31 {
                if ((n >> b) & 1) == 0 { continue }
                let x = n ^ (1 << b)
                if (x | (x + 1)) == n { ans[i] = x; break }
            }
        }
        return ans
    }
}
