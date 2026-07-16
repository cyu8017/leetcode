// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

class Solution {
    func largestNumber(_ nums: [Int]) -> String {
        let parts = nums.map(String.init).sorted { $0 + $1 > $1 + $0 }
        return parts[0] == "0" ? "0" : parts.joined()
    }
}