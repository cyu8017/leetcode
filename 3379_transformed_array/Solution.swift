// LeetCode 3379 - Transformed Array
// https://leetcode.com/problems/transformed-array/

class Solution {
    func constructTransformedArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            let j = ((i + nums[i]) % n + n) % n
            ans[i] = nums[j]
        }
        return ans
    }
}
