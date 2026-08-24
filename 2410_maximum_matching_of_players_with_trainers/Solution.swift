// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution {
    func matchPlayersAndTrainers(_ players: [Int], _ trainers: [Int]) -> Int {
        let players = players.sorted()
        let trainers = trainers.sorted()
        var i = 0, j = 0, ans = 0
        while i < players.count && j < trainers.count {
            if players[i] <= trainers[j] { ans += 1; i += 1; j += 1 }
            else { j += 1 }
        }
        return ans
    }
}
