// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum_sum_of_three_numbers_divisible_by_three/

class Solution {
    fun maximumSum(nums: IntArray): Int {
        nums.sort()
        val g = Array(3) { ArrayList<Int>() }
        for (x in nums) g[x % 3].add(x)
        var ans = 0
        for (a in 0 until 3) {
            if (g[a].isNotEmpty()) {
                val x = g[a].removeAt(g[a].size - 1)
                for (b in 0 until 3) {
                    if (g[b].isNotEmpty()) {
                        val y = g[b].removeAt(g[b].size - 1)
                        val c = (3 - (a + b) % 3) % 3
                        if (g[c].isNotEmpty()) {
                            val z = g[c][g[c].size - 1]
                            ans = maxOf(ans, x + y + z)
                        }
                        g[b].add(y)
                    }
                }
                g[a].add(x)
            }
        }
        return ans
    }
}
