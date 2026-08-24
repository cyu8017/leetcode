// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution {
    fun canTransform(start: String, result: String): Boolean {
        var a = StringBuilder()
        var b = StringBuilder()
        for (ch in start.toCharArray()) { if (ch != 'X') a.append(ch) }
        for (ch in result.toCharArray()) { if (ch != 'X') b.append(ch) }
        if (!a.toString(() == b.toString())) return false
        var i = 0
        var j = 0
        var n = start.length
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') i++
            while (j < n && result[j] == 'X') j++
            if (i == n || j == n) break
            if (start[i] != result[j]) return false
            if (start[i] == 'L' && i < j) return false
            if (start[i] == 'R' && i > j) return false
            i++
            j++
        }
        return true
    }
}
