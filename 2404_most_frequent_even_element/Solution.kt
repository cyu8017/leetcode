// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

class Solution {
    fun mostFrequentEven(nums: IntArray): Int {
        val cnt = HashMap<Int, Int>()
        var ans = -1
        var best = 0
        for (x in nums) {
            if (x % 2 != 0) continue
            val c = cnt.getOrDefault(x, 0) + 1
            cnt[x] = c
            if (c > best || (c == best && (ans == -1 || x < ans))) {
                best = c
                ans = x
            }
        }
        return ans
    }
}
