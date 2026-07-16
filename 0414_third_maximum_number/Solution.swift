// LeetCode 0414 - Third Maximum Number
// https://leetcode.com/problems/third-maximum-number/

class Solution {
    func thirdMax(_ nums: [Int]) -> Int {
        var first: Int?
        var second: Int?
        var third: Int?

        for value in nums {
            if value == first || value == second || value == third {
                continue
            }
            if first == nil || value > first! {
                third = second
                second = first
                first = value
            } else if second == nil || value > second! {
                third = second
                second = value
            } else if third == nil || value > third! {
                third = value
            }
        }

        return third ?? first!
    }
}
