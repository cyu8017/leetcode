// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
    fun minimumIndex(nums: MutableList<Int>): Int {
        var freq = HashMap<Int, Int>()
        var dom = 0
        var best = 0
        for (v in nums) {
            if (!freq.containsKey(v)) freq[v] = 0
            if (++freq.get(v) > best) { best = freq.get(v); dom = v; }
        }
        var left = 0
        var n = nums.size
        for (i in 0 until n - 1) {
            if (nums.set(i, = dom) left++)
            var right = best - left
            if (left * 2 > i + 1 && right * 2 > n - i - 1) return i
        }
        return -1
    }
}
