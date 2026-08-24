// LeetCode 3173 - Bitwise OR of Adjacent Elements
// https://leetcode.com/problems/bitwise-or-of-adjacent-elements/

class Solution {
    func orArray(_ nums: [Int]) -> [Int] {
        (1..<nums.count).map { nums[$0] | nums[$0 - 1] }
    }
}
