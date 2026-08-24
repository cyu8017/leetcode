// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

class Solution {
    fun memoize(fn: (Int) -> Int): (Int) -> Int {
        val cache = HashMap<Int, Int>()
        return { x ->
            cache[x] ?: fn(x).also { cache[x] = it }
        }
    }
}
