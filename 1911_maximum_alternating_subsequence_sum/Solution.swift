// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        var even = 0, odd = 0
        for x in nums {
            let ne = max(even, odd + x)
            let no = max(odd, even - x)
            even = ne
            odd = no
        }
        return even
    }
}
