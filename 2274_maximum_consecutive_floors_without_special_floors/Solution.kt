// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution {

    fun maxConsecutive(bottom: Int, top: Int, special: IntArray): Int {

            special.sort()
            var ans = special[0] - bottom
            for (i in 1 until special.size) { ans = maxOf(ans, special[i] - special[i - 1] - 1) }
            ans = maxOf(ans, top - special[special.size - 1])
            return ans

    }

}
