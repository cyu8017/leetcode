// LeetCode 1437 - Check If All 1's Are at Least Length K Places Away
// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var previous = -k - 1
        for (i, value) in nums.enumerated() where value == 1 {
            if i - previous <= k { return false }
            previous = i
        }
        return true
    }
}
