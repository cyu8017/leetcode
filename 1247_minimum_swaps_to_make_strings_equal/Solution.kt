// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
    fun minimumSwap(s1: String, s2: String): Int {
        var xy = 0
        var yx = 0
        for (i in s1.indices) {
            if (s1[i] == 'x' && s2[i] == 'y') xy++
            if (s1[i] == 'y' && s2[i] == 'x') yx++
        }
        if ((xy + yx) % 2 == 1) return -1
        return xy / 2 + yx / 2 + 2 * (xy % 2)
    }
}
