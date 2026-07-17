// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution {
    func canEat(_ candiesCount: [Int], _ queries: [[Int]]) -> [Bool] {
        var prefix = [0]
        prefix.reserveCapacity(candiesCount.count + 1)
        for count in candiesCount {
            prefix.append(prefix[prefix.count - 1] + count)
        }
        var ans: [Bool] = []
        ans.reserveCapacity(queries.count)
        for query in queries {
            let candyType = query[0]
            let day = query[1]
            let cap = query[2]
            let minEaten = day + 1
            let maxEaten = (day + 1) * cap
            ans.append(maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1])
        }
        return ans
    }
}
