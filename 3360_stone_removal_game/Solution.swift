// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
    func canAliceWin(_ n: Int) -> Bool {
        var n = n, take = 10, alice = true
        while n >= take && take > 0 {
            n -= take
            take -= 1
            alice = !alice
        }
        return !alice
    }
}
