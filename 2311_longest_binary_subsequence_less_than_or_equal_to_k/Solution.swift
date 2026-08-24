// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution {
    func longestSubsequence(_ s: String, _ k: Int) -> Int {
        let arr = Array(s)
        var zeros = arr.filter { $0 == "0" }.count
        var val = 0, ones = 0, pow = 1
        for i in stride(from: arr.count - 1, through: 0, by: -1) {
            if arr[i] == "1" {
                if !(pow > k || val + pow > k) {
                    val += pow
                    ones += 1
                }
            }
            if pow <= k {
                if pow > (1 << 60) { pow = k + 1 }
                else { pow <<= 1 }
            }
        }
        return zeros + ones
    }
}
