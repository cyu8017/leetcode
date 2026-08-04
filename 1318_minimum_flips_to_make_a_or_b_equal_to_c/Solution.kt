// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution {
    fun minFlips(a: Int, b: Int, c: Int): Int {
        var aa = a
        var bb = b
        var cc = c
        var flips = 0
        while (aa != 0 || bb != 0 || cc != 0) {
            val x = aa and 1
            val y = bb and 1
            val z = cc and 1
            flips += if (z == 0) x + y else if (x == 0 && y == 0) 1 else 0
            aa = aa shr 1
            bb = bb shr 1
            cc = cc shr 1
        }
        return flips
    }
}
