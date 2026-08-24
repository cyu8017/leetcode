// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

class Solution {
    fun powerfulIntegers(x: Int, y: Int, bound: Int): List<Int> {
        val ans = HashSet<Int>()
        var a = 1L
        while (a < bound) {
            var b = 1L
            while (a + b <= bound) {
                ans.add((a + b).toInt())
                if (y == 1) break
                b *= y
            }
            if (x == 1) break
            a *= x
        }
        return ans.toList()
    }
}
