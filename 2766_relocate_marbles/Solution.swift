// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

class Solution {
    func relocateMarbles(_ nums: [Int], _ moveFrom: [Int], _ moveTo: [Int]) -> [Int] {
        var pos = Set(nums)
        for i in moveFrom.indices {
            pos.remove(moveFrom[i])
            pos.insert(moveTo[i])
        }
        return pos.sorted()
    }
}
