// LeetCode 0788 - Rotated Digits
// https://leetcode.com/problems/rotated-digits/

class Solution {
    fun rotatedDigits(n: Int): Int {
        var count = 0
        for (num in 1 until = n) {
            var s = Integer.toString(num)
            var ok = true
            var changed = false
            for (ch in s.toCharArray()) {
                if (ch == '3' || ch == '4' || ch == '7') { ok = false; break; }
                if (ch == '2' || ch == '5' || ch == '6' || ch == '9') changed = true
            }
            if (ok && changed) count++
        }
        return count
    }
}
