// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution {
    func sumOddLengthSubarrays(_ arr: [Int]) -> Int {
        let n = arr.count
        var ans = 0
        for (i, x) in arr.enumerated() {
            ans += x * (((i + 1) * (n - i) + 1) / 2)
        }
        return ans
    }
}
