// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

class Solution {
    private fun depth(x0: Long): Int {
        var x = x0
        if (x == 1L) return 0
        var d = 0
        while (x > 1) {
            x = x.countOneBits().toLong()
            d++
        }
        return d
    }

    fun popcountDepth(nums: LongArray, queries: Array<LongArray>): IntArray {
        val a = nums.clone()
        val ans = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1L) {
                val l = q[1].toInt()
                val r = q[2].toInt()
                val k = q[3].toInt()
                var cnt = 0
                for (i in l..r) if (depth(a[i]) == k) cnt++
                ans.add(cnt)
            } else {
                a[q[1].toInt()] = q[2]
            }
        }
        return ans.toIntArray()
    }
}
