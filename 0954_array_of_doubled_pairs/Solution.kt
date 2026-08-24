// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

class Solution {
    fun canReorderDoubled(arr: IntArray): Boolean {
        var count = java.util.TreeMap<>()
        for (x in arr) { count.put(x, count.getOrDefault(x, 0) + 1); }
        var keys = ArrayList(count.keys)
        keys.sortBy { kotlin.math.abs(it) }
        for (x in keys) {
            var need = count[x]
            if (need == 0) continue
            if (count.getOrDefault(2 * x, 0) < need) return false
            count.put(2 * x, count[2 * x] - need)
        }
        return true
    }
}
