// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution {
    func countKDifference(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        var ans = 0
        for x in nums {
            ans += freq[x - k, default: 0]
            ans += freq[x + k, default: 0]
            freq[x, default: 0] += 1
        }
        return ans
    }
}
