// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    func dominantIndices(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0, suf = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] * (n - i - 1) > suf { ans += 1 }
                suf += nums[i]
            }
        }
        return ans
    }
}
