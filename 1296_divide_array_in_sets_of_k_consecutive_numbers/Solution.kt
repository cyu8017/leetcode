// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

import java.util.TreeMap

class Solution {
    fun isPossibleDivide(nums: IntArray, k: Int): Boolean {
        if (nums.size % k != 0) return false
        val counts = TreeMap<Int, Int>()
        for (x in nums) counts[x] = counts.getOrDefault(x, 0) + 1
        while (counts.isNotEmpty()) {
            val start = counts.firstKey()
            val amount = counts[start]!!
            if (amount == 0) {
                counts.remove(start)
                continue
            }
            for (value in start until start + k) {
                if (!counts.containsKey(value) || counts[value]!! < amount) return false
                counts[value] = counts[value]!! - amount
                if (counts[value] == 0) counts.remove(value)
            }
        }
        return true
    }
}
