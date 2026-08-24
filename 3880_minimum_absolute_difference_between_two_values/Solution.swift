// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution {
    func minAbsoluteDifference(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = n + 1
        var last = [-ans, -ans, -ans]
        for i in 0..<n {
            let x = nums[i]
            if x != 0 {
                ans = min(ans, i - last[3 - x])
                last[x] = i
            }
        }
        if ans > n { return -1 }
        return ans
    }
}
