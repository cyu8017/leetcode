// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

class Solution {
    fun countRatioSubarrays(nums: IntArray, a: Int, b: Int): Long {
        val n = nums.size
        val s = LongArray(n + 1)
        for (i in 0 until n) {
            s[i + 1] = if (nums[i] % 2 == 1) s[i] + a else s[i] - b
        }
        var st = s.copyOf()
        st.sort()
        var uniq = 0
        for (i in st.indices) {
            if (uniq == 0 || st[i] != st[uniq - 1]) st[uniq++] = st[i]
        }
        st = st.copyOf(uniq)
        val bit = BIT(st.size + 1)
        var ans = 0L
        for (v in s) {
            val x = lowerBound(st, v) + 1
            ans += bit.query(x)
            bit.update(x, 1)
        }
        return ans
    }

    private fun lowerBound(a: LongArray, x: Long): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) ushr 1
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private class BIT(val n: Int) {
        private val c = IntArray(n + 1)
        fun update(x0: Int, delta: Int) {
            var x = x0
            while (x <= n) {
                c[x] += delta
                x += x and -x
            }
        }
        fun query(x0: Int): Int {
            var x = x0
            var sum = 0
            while (x > 0) {
                sum += c[x]
                x -= x and -x
            }
            return sum
        }
    }
}
