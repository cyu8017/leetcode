// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    fun alphabetBoardPath(target: String): String {
        var row = 0
        var col = 0
        val ans = StringBuilder()
        for (ch in target) {
            val r = (ch - 'a') / 5
            val c = (ch - 'a') % 5
            while (row > r) { ans.append('U'); row-- }
            while (col > c) { ans.append('L'); col-- }
            while (row < r) { ans.append('D'); row++ }
            while (col < c) { ans.append('R'); col++ }
            ans.append('!')
        }
        return ans.toString()
    }
}
