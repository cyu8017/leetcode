// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution {
    func mostVisited(_ n: Int, _ rounds: [Int]) -> [Int] {
        let start = rounds[0], end = rounds.last!
        if start <= end { return Array(start...end) }
        return Array(1...end) + Array(start...n)
    }
}
