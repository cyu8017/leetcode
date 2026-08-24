// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution {
    fun kthSmallestPrimeFraction(arr: IntArray, k: Int): IntArray {
        val n = arr.size
        val heap = PriorityQueue<IntArray> { a, b ->
            java.lang.Double.compare(arr[a[0]].toDouble() / arr[a[1]], arr[b[0]].toDouble() / arr[b[1]])
        }
        for (i in 0 until n - 1) heap.offer(intArrayOf(i, n - 1))
        repeat(k - 1) {
            val top = heap.poll()
            val i = top[0]
            val j = top[1]
            if (j - 1 > i) heap.offer(intArrayOf(i, j - 1))
        }
        val top = heap.poll()
        return intArrayOf(arr[top[0]], arr[top[1]])
    }
}
