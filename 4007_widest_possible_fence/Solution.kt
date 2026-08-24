// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

class Solution {
    fun maximumWidth(planks: IntArray): Int {
        val cnt = HashMap<Int, Int>()
        for (x in planks) cnt[x] = cnt.getOrDefault(x, 0) + 1
        val t = HashMap<Int, Int>()
        var ans = 0
        for ((x, v1) in cnt) {
            t[x] = t.getOrDefault(x, 0) + v1
            ans = maxOf(ans, t[x]!!)
            t[x * 2] = t.getOrDefault(x * 2, 0) + v1 / 2
            ans = maxOf(ans, t[x * 2]!!)
            for ((y, v2) in cnt) {
                if (y > x) {
                    val key = x + y
                    t[key] = t.getOrDefault(key, 0) + minOf(v1, v2)
                    ans = maxOf(ans, t[key]!!)
                }
            }
        }
        return ans
    }
}
