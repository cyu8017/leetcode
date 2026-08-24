// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

import java.util.PriorityQueue

class Solution {
    private lateinit var cnt: HashMap<Int, Int>
    private lateinit var pq: PriorityQueue<IntArray>

    private fun getMode(): Long {
        while (true) {
            val top = pq.peek()
            val freq = top[0]
            val `val` = -top[1]
            if (cnt.getOrDefault(`val`, 0) == freq) return 1L * freq * `val`
            pq.poll()
        }
    }

    fun modeWeight(nums: IntArray, k: Int): Long {
        cnt = HashMap()
        pq = PriorityQueue { a, b ->
            if (a[0] != b[0]) b[0].compareTo(a[0]) else a[1].compareTo(b[1])
        }
        for (i in 0 until k) {
            val x = nums[i]
            cnt.merge(x, 1) { a, b -> a + b }
            pq.offer(intArrayOf(cnt[x]!!, -x))
        }
        var ans = getMode()
        for (i in k until nums.size) {
            val x = nums[i]
            val y = nums[i - k]
            cnt.merge(x, 1) { a, b -> a + b }
            cnt.merge(y, -1) { a, b -> a + b }
            pq.offer(intArrayOf(cnt[x]!!, -x))
            pq.offer(intArrayOf(cnt.getOrDefault(y, 0), -y))
            ans += getMode()
        }
        return ans
    }
}
