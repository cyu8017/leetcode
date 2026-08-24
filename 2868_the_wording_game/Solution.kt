// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

class Solution {
    fun canAliceWin(a: Array<String>, b: Array<String>): Boolean {
        var i = 0
        var j = 0
        var last = 0
        var alice = true
        while (true) {
            if (alice) {
                while (i < a.size && a[i][0] <= last) i++
                if (i == a.size) return false
                last = a[i][a[i].length - 1]
                i++
            } else {
                while (j < b.size && b[j][0] <= last) j++
                if (j == b.size) return true
                last = b[j][b[j].length - 1]
                j++
            }
            alice = !alice
        }
    }
}
