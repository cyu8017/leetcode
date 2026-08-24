// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution {

    fun largestCombination(candidates: IntArray): Int {

            var ans = 0
            for (bit in 0 until 24) {
                var cnt = 0
                for (x in candidates) if (((x >> bit) & 1) != 0) cnt++
                ans = maxOf(ans, cnt)
            }
            return ans

    }

}
