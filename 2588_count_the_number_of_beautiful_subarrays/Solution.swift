// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

class Solution {
    func beautifulSubarrays(_ nums: [Int]) -> Int {
        var freq = [Int: Int]()
        freq[0] = 1
        var xorv = 0, ans = 0
        for x in nums {
            xorv ^= x
            ans += freq[xorv, default: 0]
            freq[xorv, default: 0] += 1
        }
        return ans
    }
}
