// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

class Solution {
    func twoEggDrop(_ n: Int) -> Int {
        var moves = 0
        var covered = 0
        while covered < n {
            moves += 1
            covered += moves
        }
        return moves
    }
}
