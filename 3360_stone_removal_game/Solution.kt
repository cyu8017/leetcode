// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

class Solution {
    fun canAliceWin(n: Int): Boolean {
        var take = 10
        var alice = true
        while (n >= take && take > 0) {
            n -= take
            take--
            alice = !alice
        }
        return !alice
    }
}
