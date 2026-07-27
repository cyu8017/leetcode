// LeetCode 1608 - Special Array With X Elements Greater Than or Equal X
// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution {
    func specialArray(_ nums: [Int]) -> Int {
        for x in 0...nums.count {
            if nums.filter({ $0 >= x }).count == x { return x }
        }
        return -1
    }
}
