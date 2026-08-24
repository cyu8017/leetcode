// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

class Solution {
    func distributeCandies(_ candyType: [Int]) -> Int {
        return min(Set(candyType).count, candyType.count / 2)
    }
}
