// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution {
    func maximumGroups(_ grades: [Int]) -> Int {
        let n = grades.count
        var k = 0
        while (k + 1) * (k + 2) / 2 <= n { k += 1 }
        return k
    }
}
