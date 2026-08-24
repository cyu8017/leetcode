// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution {
    func numSubarraysWithSum(_ nums: [Int], _ goal: Int) -> Int {
        var count = [0: 1]
        var prefix = 0, ans = 0
        for x in nums {
            prefix += x
            ans += count[prefix - goal, default: 0]
            count[prefix, default: 0] += 1
        }
        return ans
    }
}
