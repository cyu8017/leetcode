// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

class Solution {
    fun maximumLength(nums: IntArray): Int {
        val cnt = HashMap<Long, Int>()
        for (x in nums) {
            val key = x.toLong()
            cnt[key] = cnt.getOrDefault(key, 0) + 1
        }
        val ones = cnt.getOrDefault(1L, 0)
        var ans = ones - ((ones % 2) xor 1)
        cnt.remove(1L)
        val keys = ArrayList(cnt.keys)
        for (start in keys) {
            var x = start
            var t = 0
            while (cnt.getOrDefault(x, 0) > 1) {
                x = x * x
                t += 2
            }
            if (cnt.getOrDefault(x, 0) > 0) t += 1
            else t -= 1
            ans = maxOf(ans, t)
        }
        return ans
    }
}
