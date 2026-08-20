// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution {
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        let maximum = candies.max()!
        return candies.map { $0 + extraCandies >= maximum }
    }
}
