// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution {
    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var vis = Set<Int>()
            var cnt = [0, 0]
            for j in i..<n {
                if !vis.contains(nums[j]) {
                    vis.insert(nums[j])
                    cnt[nums[j] & 1] += 1
                }
                if cnt[0] == cnt[1] { ans = max(ans, j - i + 1) }
            }
        }
        return ans
    }
}
