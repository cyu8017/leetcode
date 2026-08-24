// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

class Solution {
    private class Fenwick(n: Int) {
        private val bit = IntArray(n + 2)
        fun add(i0: Int, v: Int) {
            var i = i0
            while (i < bit.size) {
                bit[i] += v
                i += i and -i
            }
        }
        fun sum(i0: Int): Int {
            var i = i0
            var s = 0
            while (i > 0) {
                s += bit[i]
                i -= i and -i
            }
            return s
        }
    }

    fun kBigIndices(nums: IntArray, k: Int): Int {
        val n = nums.size
        val uniq = nums.copyOf()
        uniq.sort()
        var m = 0
        for (i in uniq.indices) {
            if (i == 0 || uniq[i] != uniq[i - 1]) uniq[m++] = uniq[i]
        }
        val rank = HashMap<Int, Int>()
        for (i in 0 until m) rank[uniq[i]] = i + 1
        val left = IntArray(n)
        val right = IntArray(n)
        var ft = Fenwick(m)
        for (i in 0 until n) {
            val r = rank[nums[i]]!!
            left[i] = ft.sum(r - 1)
            ft.add(r, 1)
        }
        ft = Fenwick(m)
        for (i in n - 1 downTo 0) {
            val r = rank[nums[i]]!!
            right[i] = ft.sum(r - 1)
            ft.add(r, 1)
        }
        var ans = 0
        for (i in 0 until n) if (left[i] >= k && right[i] >= k) ans++
        return ans
    }
}
