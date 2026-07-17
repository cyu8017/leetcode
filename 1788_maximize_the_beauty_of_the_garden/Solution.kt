// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

class Solution {
    fun maximumBeauty(flowers: IntArray): Int {
        val first = HashMap<Int, Int>()
        val prefix = LongArray(flowers.size + 1)
        for (i in flowers.indices) {
            prefix[i + 1] = prefix[i] + maxOf(flowers[i], 0)
        }
        var best = Long.MIN_VALUE
        for (i in flowers.indices) {
            val value = flowers[i]
            val left = first[value]
            if (left != null) {
                val between = prefix[i] - prefix[left + 1]
                best = maxOf(best, flowers[left].toLong() + flowers[i] + between)
            } else {
                first[value] = i
            }
        }
        return best.toInt()
    }
}
