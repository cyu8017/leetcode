// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

class Solution {
    func distributeCandies(_ candies: Int, _ num_people: Int) -> [Int] {
        var candies = candies
        var ans = [Int](repeating: 0, count: num_people)
        var give = 1
        var i = 0
        while candies > 0 {
            let take = min(give, candies)
            ans[i] += take
            candies -= take
            give += 1
            i = (i + 1) % num_people
        }
        return ans
    }
}
