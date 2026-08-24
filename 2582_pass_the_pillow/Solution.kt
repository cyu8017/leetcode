// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

class Solution {
    fun passThePillow(n: Int, time: Int): Int {
        var cycle = 2 * (n - 1)
        var t = time % cycle
        if (t < n) return 1 + t
        return n - (t - (n - 1))
    }
}
