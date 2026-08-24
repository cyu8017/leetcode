// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution {
    fun canChange(start: String, target: String): Boolean {
        val n = start.length
        var i = 0
        var j = 0
        while (i < n || j < n) {
            while (i < n && start[i] == '_') i++
            while (j < n && target[j] == '_') j++
            if (i == n || j == n) return i == n && j == n
            if (start[i] != target[j]) return false
            if (start[i] == 'L' && i < j) return false
            if (start[i] == 'R' && i > j) return false
            i++
            j++
        }
        return true
    }
}
