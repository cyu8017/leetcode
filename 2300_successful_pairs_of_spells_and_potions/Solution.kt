// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution {

    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {

            potions.sort()
            var m = potions.size
            var ans = IntArray(spells.size)
            for (i in 0 until spells.size) {
                var lo = 0; var hi = m
                while (lo < hi) {
                    var mid = (lo + hi) / 2
                    if (spells[i] * potions[mid] >= success) hi = mid
                    else lo = mid + 1
                }
                ans[i] = m - lo
            }
            return ans

    }

}
