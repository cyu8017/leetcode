// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/


class Solution {
    fun minSteps(n: Int): Int {
        var remain = n
        var steps = 0
        var d = 2
        while (d * d <= remain) {
            while (remain % d == 0) {
                steps += d
                remain /= d
            }
            d++
        }
        if (remain > 1) steps += remain
        return steps
    }
}
