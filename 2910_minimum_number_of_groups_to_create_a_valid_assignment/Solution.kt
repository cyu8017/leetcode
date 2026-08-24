// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

class Solution {
    fun minGroupsForValidAssignment(balls: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (b in balls) freq[b] = freq.getOrDefault(b, 0) + 1
        val counts = ArrayList<Int>()
        var minF = 1 shl 30
        for (f in freq.values) {
            counts.add(f)
            if (f < minF) minF = f
        }
        for (size in minF downTo 1) {
            var ok = true
            var groups = 0
            for (c in counts) {
                val rem = c % (size + 1)
                val g2 = c / (size + 1)
                when {
                    rem == 0 -> groups += g2
                    size - rem <= g2 -> groups += g2 + 1
                    else -> {
                        ok = false
                        break
                    }
                }
            }
            if (ok) return groups
        }
        return balls.size
    }
}
