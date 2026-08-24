// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    fun dietPlanPerformance(calories: IntArray, k: Int, lower: Int, upper: Int): Int {
        var window = 0
        for (i in 0 until k) window += calories[i]
        var ans = 0
        if (window < lower) ans-- else if (window > upper) ans++
        for (i in k until calories.size) {
            window += calories[i] - calories[i - k]
            if (window < lower) ans-- else if (window > upper) ans++
        }
        return ans
    }
}
