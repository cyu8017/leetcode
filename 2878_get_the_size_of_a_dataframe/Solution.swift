// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/
// Pandas stand-in.

class Solution {
    func getDataframeSize(_ players: [[Any]]) -> [Int] {
        if players.isEmpty { return [0, 0] }
        return [players.count, players[0].count]
    }
}
