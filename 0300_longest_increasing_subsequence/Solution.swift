// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        var piles: [Int] = []
        for num in nums {
            var left = 0
            var right = piles.count
            while left < right {
                let mid = (left + right) / 2
                if piles[mid] < num {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if left == piles.count {
                piles.append(num)
            } else {
                piles[left] = num
            }
        }
        return piles.count
    }
}
