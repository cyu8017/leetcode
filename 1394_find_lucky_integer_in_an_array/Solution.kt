// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution {
    fun findLucky(arr: IntArray): Int {
        val cnt = mutableMapOf<Int, Int>()
        for (x in arr) cnt[x] = cnt.getOrDefault(x, 0) + 1
        var ans = -1
        for ((x, c) in cnt) if (x == c) ans = maxOf(ans, x)
        return ans
    }
}
