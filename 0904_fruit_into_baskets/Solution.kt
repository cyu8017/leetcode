// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

class Solution {
    fun totalFruit(fruits: IntArray): Int {
        var count = HashMap()
        var left = 0
        var ans = 0
        for (right in 0 until fruits.size) {
            count.put(fruits[right], count.getOrDefault(fruits[right], 0) + 1)
            while (count.size > 2) {
                var c = count[fruits[left]] - 1
                if (c == 0) count.remove(fruits[left])
                else count.put(fruits[left], c)
                left++
            }
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }
}
