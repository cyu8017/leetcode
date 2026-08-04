// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution {
    fun avoidFlood(rains: IntArray): IntArray {
        val ans = IntArray(rains.size) { -1 }
        val full = HashMap<Int, Int>()
        val dry = java.util.TreeSet<Int>()
        for (i in rains.indices) {
            val lake = rains[i]
            if (lake == 0) {
                dry.add(i)
                ans[i] = 1
            } else {
                if (lake in full) {
                    val day = dry.higher(full[lake]!!) ?: return IntArray(0)
                    ans[day] = lake
                    dry.remove(day)
                }
                full[lake] = i
            }
        }
        return ans
    }
}
