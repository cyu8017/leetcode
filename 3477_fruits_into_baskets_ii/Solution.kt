// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

class Solution {
    fun numOfUnplacedFruits(fruits: IntArray, baskets: IntArray): Int {
        var used = BooleanArray(baskets.size)
        var unplaced = 0
        for (f in fruits) {
            var placed = false
            for (j in 0 until baskets.size) {
                if (!used[j] && baskets[j] >= f) {
                    used[j] = true
                    placed = true
                    break
                }
            }
            if (!placed) unplaced++
        }
        return unplaced
    }
}
