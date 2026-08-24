// LeetCode 2765 - Longest Alternating Subarray
// https://leetcode.com/problems/longest-alternating-subarray/

class Solution {
    func alternatingSubarray(_ nums: [Int]) -> Int {
        var ans = -1
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                let expect = (j - i) % 2 == 0 ? -1 : 1
                if nums[j] - nums[j - 1] != expect { break }
                if nums[i + 1] - nums[i] != 1 { break }
                ans = max(ans, j - i + 1)
            }
        }
        return ans
    }
}
