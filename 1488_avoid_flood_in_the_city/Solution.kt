// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

import java.util.TreeSet

class Solution {
    fun avoidFlood(rains: IntArray): IntArray {
        val ans = IntArray(rains.size) { -1 }
        val full = mutableMapOf<Int, Int>()
        val dry = TreeSet<Int>()
        for (i in rains.indices) {
            val lake = rains[i]
            if (lake == 0) {
                dry.add(i)
                ans[i] = 1
            } else {
                if (lake in full) {
                    val day = dry.higher(full[lake]!!) ?: return intArrayOf()
                    ans[day] = lake
                    dry.remove(day)
                }
                full[lake] = i
            }
        }
        return ans
    }
}
