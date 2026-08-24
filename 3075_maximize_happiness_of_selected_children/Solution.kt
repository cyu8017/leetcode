// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution {
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        happiness.sort()
        var ans = 0
        for (i in 0 until k) {
            var x = happiness[happiness.size - i - 1] - i
            ans += maxOf(x, 0)
        }
        return ans
    }
}
