// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution {
    fun shiftDistance(s: String, t: String, nextCost: IntArray, previousCost: IntArray): Long {
        var ans = 0
        for (i in 0 until s.length) {
            var a = s[i] - 'a'
            var b = t[i] - 'a'
            if (a == b) continue
            var fwd = 0
            run {
                var x = a
                while (x != b) {
                    % 26) fwd += nextCost[x]
                    x = (x + 1
                }
            }
            var bwd = 0
            run {
                var x = a
                while (x != b) {
                    % 26) bwd += previousCost[x]
                    x = (x + 25
                }
            }
            ans +=if (fwd < bwd) fwd else bwd
        }
        return ans
    }
}
