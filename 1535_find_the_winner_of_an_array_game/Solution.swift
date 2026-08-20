// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution {
    func getWinner(_ arr: [Int], _ k: Int) -> Int {
        var champion = arr[0], wins = 0
        for i in 1..<arr.count {
            if champion > arr[i] {
                wins += 1
            } else {
                champion = arr[i]
                wins = 1
            }
            if wins == k { break }
        }
        return champion
    }
}
