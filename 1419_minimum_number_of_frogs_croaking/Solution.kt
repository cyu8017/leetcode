// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution {
    fun minNumberOfFrogs(croakOfFrogs: String): Int {
        val order = hashMapOf('c' to 0, 'r' to 1, 'o' to 2, 'a' to 3, 'k' to 4)
        val counts = IntArray(5)
        var active = 0
        var answer = 0
        for (char in croakOfFrogs) {
            val i = order[char] ?: return -1
            if (i > 0 && counts[i - 1] == 0) return -1
            if (i > 0) counts[i - 1]--
            counts[i]++
            if (i == 0) {
                active++
                answer = maxOf(answer, active)
            } else if (i == 4) {
                counts[4]--
                active--
            }
        }
        return if (active == 0) answer else -1
    }
}
