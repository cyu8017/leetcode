// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

import java.util.PriorityQueue

class Solution {
    class SparseTableRMQ(data: IntArray) {
        private val n = data.size
        private var maxLog = 0
        private val fMax: Array<IntArray>
        private val fMin: Array<IntArray>
        private val lg: IntArray

        init {
            while ((1 shl maxLog) <= n) maxLog++
            maxLog++
            fMax = Array(n) { IntArray(maxLog) }
            fMin = Array(n) { IntArray(maxLog) }
            lg = IntArray(n + 1)
            for (i in 2..n) lg[i] = lg[i shr 1] + 1
            for (i in 0 until n) {
                fMax[i][0] = data[i]
                fMin[i][0] = data[i]
            }
            for (j in 1 until maxLog) {
                var i = 0
                while (i <= n - (1 shl j)) {
                    fMax[i][j] = maxOf(fMax[i][j - 1], fMax[i + (1 shl (j - 1))][j - 1])
                    fMin[i][j] = minOf(fMin[i][j - 1], fMin[i + (1 shl (j - 1))][j - 1])
                    i++
                }
            }
        }

        fun queryMax(l: Int, r: Int): Int {
            val k = lg[r - l + 1]
            return maxOf(fMax[l][k], fMax[r - (1 shl k) + 1][k])
        }

        fun queryMin(l: Int, r: Int): Int {
            val k = lg[r - l + 1]
            return minOf(fMin[l][k], fMin[r - (1 shl k) + 1][k])
        }
    }

    fun maxTotalValue(nums: IntArray, k: Int): Long {
        val n = nums.size
        val st = SparseTableRMQ(nums)
        val pq = PriorityQueue<LongArray>(compareByDescending { it[0] })
        for (l in 0 until n) {
            val `val` = st.queryMax(l, n - 1).toLong() - st.queryMin(l, n - 1)
            pq.offer(longArrayOf(`val`, l.toLong(), (n - 1).toLong()))
        }
        var ans = 0L
        for (i in 0 until k) {
            val top = pq.poll()
            val `val` = top[0]
            val l = top[1].toInt()
            val r = top[2].toInt()
            ans += `val`
            if (r > l) {
                val nextVal = st.queryMax(l, r - 1).toLong() - st.queryMin(l, r - 1)
                pq.offer(longArrayOf(nextVal, l.toLong(), (r - 1).toLong()))
            }
        }
        return ans
    }
}
