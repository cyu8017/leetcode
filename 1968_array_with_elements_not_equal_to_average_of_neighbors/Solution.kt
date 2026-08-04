// LeetCode 1968
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution {
    fun rearrangeArray(nums: IntArray): IntArray {
        nums.sort()
        val n = nums.size
        val mid = (n + 1) / 2
        val small = nums.copyOfRange(0, mid)
        val large = nums.copyOfRange(mid, n)
        val ans = mutableListOf<Int>()
        var i = 0
        var j = 0
        while (i < small.size || j < large.size) {
            if (i < small.size) ans.add(small[i++])
            if (j < large.size) ans.add(large[j++])
        }
        return ans.toIntArray()
    }
}
