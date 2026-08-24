// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

class Solution {
    func maximumSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        var p: [Int: Int] = [nums[0]: 0]
        var s = 0
        let n = nums.count
        var ans = Int.min
        for i in 0..<n {
            s += nums[i]
            if let v = p[nums[i] - k] { ans = max(ans, s - v) }
            if let v = p[nums[i] + k] { ans = max(ans, s - v) }
            if i + 1 == n { break }
            if let old = p[nums[i + 1]] {
                if s < old { p[nums[i + 1]] = s }
            } else {
                p[nums[i + 1]] = s
            }
        }
        return ans == Int.min ? 0 : ans
    }
}
