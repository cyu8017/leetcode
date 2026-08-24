// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

class Solution {
    fun miceAndCheese(reward1: IntArray, reward2: IntArray, k: Int): Int {
        val n = reward1.size
        val diff = IntArray(n)
        var ans = 0
        for (i in 0 until n) {
            ans += reward2[i]
            diff[i] = reward1[i] - reward2[i]
        }
        diff.sortDescending()
        for (i in 0 until k) ans += diff[i]
        return ans
    }
}
