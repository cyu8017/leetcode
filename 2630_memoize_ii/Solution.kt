// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

class Solution {
    fun memoizeII(fn: (IntArray) -> Int): (IntArray) -> Int {
        val cache = HashMap<String, Int>()
        return { args ->
            val sb = StringBuilder()
            for (a in args) {
                sb.append('|')
                sb.append(a)
            }
            val k = sb.toString()
            cache[k] ?: fn(args).also { cache[k] = it }
        }
    }
}
